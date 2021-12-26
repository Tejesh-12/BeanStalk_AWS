
!pip install boto3
import boto3

access_id_key = ""
secret_access_key=""
session_token_key = ""

boto3client = boto3.client('elasticbeanstalk',region_name="us-east-1",
                            aws_access_key_id=access_id_key,
                            aws_secret_access_key=secret_access_key,
                            aws_session_token=session_token_key
                           
                           )




boto3client.create_application_version(
    ApplicationName='myapp123',
    AutoCreateApplication=True,
    Description='my-app-v1',
    Process=True,
    SourceBundle={
        'S3Bucket': 'tejeshpersonal',
        'S3Key': '',
    },
    VersionLabel='v1',
)

import time
time.sleep(10)

response = boto3client.create_environment(
    ApplicationName='myapp123',
    CNAMEPrefix='my-app-link1234',
    EnvironmentName='my-env',
    SolutionStackName='64bit Amazon Linux 2 v4.2.5 running Tomcat 8.5 Corretto 11',
    VersionLabel='v1',
    OptionSettings=[
        {
            'Namespace': 'aws:autoscaling:launchconfiguration',
            'OptionName': 'IamInstanceProfile',
            'Value': 'EMR_EC2_DefaultRole',
            
            
        },
        {
            'Namespace': 'aws:autoscaling:launchconfiguration',
            'OptionName': 'InstanceType',
            'Value': 't2.micro',
            
        },
        {
            'Namespace': 'aws:autoscaling:launchconfiguration',
            'OptionName': 'EC2KeyName',
            'Value':  'CS351-CG31',
            
        },
        {
            'Namespace': 'aws:autoscaling:launchconfiguration',
            'OptionName': 'ImageId',
            'Value': 'ami-0c2b8ca1dad447f8a',
            
        },
        {
            'Namespace': 'aws:autoscaling:launchconfiguration',
            'OptionName': 'SecurityGroups',
            'Value': "CS351-CG31-SG",
        },
        {
            
            'Namespace': 'aws:autoscaling:trigger',
            'OptionName': 'BreachDuration',
            'Value': '1',
            
            
            
        },
        {
            'Namespace': 'aws:autoscaling:trigger',
            'OptionName': 'Statistic',
            'Value': 'Average',
            
        },
        {
            'Namespace': 'aws:autoscaling:trigger',
            'OptionName': 'Unit',
            'Value': 'Percent',
             
        },
        {
            'Namespace': 'aws:autoscaling:trigger',
            'OptionName': 'EvaluationPeriods',
            'Value': '1',
               
        },
        {
            'Namespace': 'aws:autoscaling:trigger',
            'OptionName': 'Period',
            'Value': '1',
            
        },
        {
            'Namespace': 'aws:autoscaling:trigger',
            'OptionName': 'UpperThreshold',
            'Value': '70',
            
        },
        {
            'Namespace': 'aws:autoscaling:trigger',
            'OptionName': 'UpperBreachScaleIncrement',
            'Value': '1',
            
        },
        {
            'Namespace': 'aws:autoscaling:trigger',
            'OptionName': 'MeasureName',
            'Value': 'CPUUtilization',
            
        },
        {
            'Namespace': 'aws:autoscaling:trigger',
            'OptionName': 'LowerThreshold',
            'Value': '30',
             
        },
        {
            'Namespace': 'aws:autoscaling:trigger',
            'OptionName': 'LowerBreachScaleIncrement',
            'Value': '-1', 
        },
        {
            'Namespace': 'aws:autoscaling:asg',
            'OptionName': 'Availability Zones',
            'Value': 'Any 2',
            
        },
        {
            'Namespace': 'aws:autoscaling:asg',
            'OptionName': 'MaxSize',
            'Value': '3',
            
        },
        {
            'Namespace': 'aws:autoscaling:asg',
            'OptionName': 'MinSize',
            'Value': '1',
        }
        
        
        

        

        
    ]
)

