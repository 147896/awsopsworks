AWS OpsWorks - Python Boto3 to integrate with aws cloudformation documentation.
Also, there are implementations to automate the OpenAM (SSO Application, Authentication, Authotization) and OpenDJ (Repository LDAP to the OpenAM), 
deployments process.

This scenario focus in the integration with aws opsworks via python script using boto3 library.

Steps as:
  1) Create App in AWS Opsworks (all parameters).
  2) Zipping and Uploading files in AWS S3 (basically yaml files).
  3) Create tree in OpenDJ (require to the OpenAM authentication and authorization).
  4) Create Realm and Policies in OpenAM (OpenAM segmentation domain).


Output the stack.py script.:
.:HELP:. :Python Script:
                   Automate the following steps:
                   - AWS Opsworks,
                   - Docker compose file manipulation,
                   - AWS bucket s3,
                   - OpenAM/OpenDJ

          -i | --stackid   # StackID
          -s | --shortname # Short Name
          -a | --appname   # App Name
          -e | --stackenv  # Environment - dsv|hml|prd
          -r | --realm     # OpenAM Realm Name
          -h | --help      # Help

          ./stack.py --stackid=<stackid> --shortname=<shortname> --appname=<appname> --stackenv=<environment> [dsv|hml|prd] --realm=<oam realm>
                     -i <stackid> -s <shortname> -a <appname> -e <environment> [dsv|hml|prd] -r <oam realm>

          Describes AWS Opsworks Stacks, example.: find stackId
                - aws opsworks --region sa-east-1 describe-stacks
