import os
import boto3

class Assignment7():
    '''
    pushAFile method is used to take input of the filename and perform git git add, git commit and git push commands
    '''
    def pushAFile(self, filename):
        commands = [("git add " + filename),
                    ("git commit -m\"commiting from pycode\" "), ("git push")]
        for i in commands:
            os.system(i)
            print("File Added and commited")
    '''
        create_ec2_launch_template accepts object of boto3.client('ec2') and is used to create the launch templte in the EC2 environment 
    '''
    def create_ec2_launch_template(self,ec2_client):
        print("Creating the Launch Templates : STARTED ")
        tname = 'a7_launch_Template'
        with open("userdata64.txt", "r") as fp:
            userdata64 = fp.read()
        try:
            response = ec2_client.create_launch_template(
                LaunchTemplateName=tname,
                LaunchTemplateData={
                    'ImageId': 'ami-00399ec92321828f5',
                    'InstanceType' : "t2.micro",
                    'KeyName' : "ec2-key",
                    'UserData': userdata64,
                    'SecurityGroupIds': ["sg-27d0d06f"]
                }
            )
            tid = response['LaunchTemplate']['LaunchTemplateId']
            print("Launch template created with ID:{} and Name:{}".format(tid, tname ))
            return tid, tname
        except Exception as e:
            response = ec2_client.describe_launch_templates(
                LaunchTemplateNames=[
                    tname,
                ]
            )
            tid = response['LaunchTemplates'][0]['LaunchTemplateId']
            return tid, tname
    '''
        create_ec2_auto_scaling_group is used to create the auto scalling group in the EC2 environment. It calls create_ec2_launch_template for creating a template
        and assigns it to the auto scalling group. We need to set the following variables vpc_id, subnet_id, az 
    '''
    def create_ec2_auto_scaling_group(self):
        ec2_client = boto3.client('ec2')
        print ("EC2 creation started")
        launch_template_id, launch_template_name = self.create_ec2_launch_template(ec2_client)
        vpc_id, subnet_id, az = "vpc-e406668f","subnet-37860e5c","us-east-2a"
        client = boto3.client('autoscaling')
        response = client.create_auto_scaling_group(
            AutoScalingGroupName='a7_autoscalling',
            LaunchTemplate={
                'LaunchTemplateId': launch_template_id,
            },
            MinSize=2,
            MaxSize=3,
            DesiredCapacity=2,
            AvailabilityZones=[
                az,
            ]
        )

if __name__ == "__main__":
    '''
        Creates object of the class Assignment7 
    '''
    
    gap = Assignment7()

    '''
        Api call to push files to github
    '''
    gap.pushAFile(".")
    print("Starting to create resources")
    '''
        API call to create auto scalling group 
    '''
    gap.create_ec2_auto_scaling_group()
    print("Operation finished")

    
