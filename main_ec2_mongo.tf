provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "mongo_instance" {
  ami           = "ami-0c55b159cbfafe1f0"  # Replace with your preferred MongoDB AMI
  instance_type = "t2.micro"
  key_name      = "sabaa_mongo"  # Replace with your key name

  user_data = <<-EOF
    #!/bin/bash
    cat <<EOT > /etc/yum.repos.d/mongodb-org-6.0.repo
    [mongodb-org-7.0]
    name=MongoDB Repository
    baseurl=https://repo.mongodb.org/yum/amazon/2023/mongodb-org/7.0/x86_64/
    gpgcheck=1
    enabled=1
    gpgkey=https://pgp.mongodb.com/server-7.0.asc
    EOT
    sudo yum install -y mongodb-org
    sudo systemctl start mongod
    sudo systemctl enable mongod
    sudo systemctl status mongod
  EOF

  tags = {
    Name = "MongoDB-Instance"
  }
}
