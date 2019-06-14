import pulumi
from pulumi_aws import ec2

size = 't2.micro'
ami_id = 'ami-0475f60cdd8fd2120' # us-west-2

group = ec2.SecurityGroup('web-secgrp',
    description='Enable HTTP access',
    ingress=[
        { 'protocol': 'tcp', 'from_port': 80, 'to_port': 80, 'cidr_blocks': ['0.0.0.0/0'] }
    ])

user_data = """
#!/bin/bash
echo "Hello, World!" > index.html
nohup python -m SimpleHTTPServer 80 &
"""

server = ec2.Instance('web-server-www',
    instance_type=size,
    security_groups=[group.name],
    user_data=user_data,
    ami=ami_id)

pulumi.export('public_ip', server.public_ip)
