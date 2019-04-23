#!/usr/bin/env python
# --*-- encoding: utf-8 --*--
# Python script to create, deploy, update and delete APP in the AWS Opsworks.
# Also, will be used to automate the manual operations, as: 
#   - OpenDJ/OpenAM
#   - AWS s3 
#   - docker compose file
# created in 2018-11-14, by Gabriel Ribas (gabriel.ribass@gmail.com - python developer)
# desv stackid=45c98eae-2ae4-4789-995d-9a43e956663c
import boto3, botocore, json, getopt, sys, os
from credentials import clientops

def usage():
   print(
         ".:HELP:. :Python Script:\n\
		   Automate the following steps:\n\
		   - AWS Opsworks,\n \
	           - Docker compose file manipulation,\n\
		   - AWS bucket s3,\n\
                   - OpenAM/OpenDJ\n\n\
	  -i | --stackid   # StackID\n\
	  -s | --shortname # Short Name\n\
	  -a | --appname   # App Name\n\
	  -e | --stackenv  # Environment - dsv|hml|prd\n\
	  -r | --realm     # OpenAM Realm Name\n\
          -h | --help      # Help\n\n\
          ./stack.py --stackid=<stackid> --shortname=<shortname> --appname=<appname> --stackenv=<environment> [dsv|hml|prd] --realm=<oam realm>\n\
	             -i <stackid> -s <shortname> -a <appname> -e <environment> [dsv|hml|prd] -r <oam realm>\n\n\
          Describes AWS Opsworks Stacks, example.: find stackId\n\
		- aws opsworks --region sa-east-1 describe-stacks"
   )

try:
   opts, args = getopt.getopt(sys.argv[1:], "hi:s:a:e:r:", ["help", "stackid=", "shortname=", "appname=", "stackenv=", "realm="])
   if opts[0][1] and opts[1][1] and opts[2][1] and opts[3][1] and opts[4][1]:
     stackid, shortname, appname, stackenv, realm = opts[0][1], opts[1][1], opts[2][1], opts[3][1], opts[4][1]
   elif not opts:
      usage()
      sys.exit(2)
except getopt.GetoptError as err:
   usage()
   sys.exit(2)
except KeyError:
   usage()
   sys.exit(2)
except IndexError:
   usage()
   sys.exit(2)
   
# manipulation docker compose file
def docker_compose(APPNAME, ENVNAME):
   os.system('sed "s/APPNAME/%s/g;s/ENVNAME/%s/g" docker-compose-template.yml \
              > docker-compose.yml ; zip apps/%s docker-compose.yml \
              ; rm -f docker-compose.yml' %(APPNAME, ENVNAME, APPNAME)
             )

# Opsworks stack create app
def response( StackId, Shortname, Name, Environment ):

		clientops.create_app(
		StackId='%s' %(StackId),
		Shortname='%s' %(Shortname),
		Name='%s' %(Name),
		Description='string',
		DataSources=[
			{	
			'Type': 'None',
			'Arn': 'No',
			'DatabaseName': 'No'
			},
		],
		Type='other',
		AppSource={
			'Type': 's3',
			'Url': 'https://s3-sa-east-1.amazonaws.com/unimedbh/docker/application/%s/%s.zip' %(Environment, Shortname)
			},
		Environment=[
			{
			'Key': 'priority',
			'Value': '5',
			},
			{
			'Key': 'target',
			'Value': 'master'
			},
		]

	       )

try:
   response(stackid, shortname, appname, stackenv)
   print("App {} created".format(appname))

   docker_compose(appname, stackenv)
   print("Setting {} docker-compose.yml file".format(appname))   
   

except clientops.exceptions.ResourceNotFoundException as e:
   print("Resource Not Found or stackID is wrong..")

except clientops.exceptions.ValidationException as e:
   print("Resource already exists or permission denied")

