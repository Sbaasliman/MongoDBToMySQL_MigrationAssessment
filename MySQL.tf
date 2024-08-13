provider "aws" {
  region = "us-east-1"
}


resource "aws_db_subnet_group" "default" {
  name       = "my-db-subnet-group"
  subnet_ids = ["subnet-0ae7e63fe9dd28dd4", "subnet-0822a00bb18608e98"]  # Replace with your actual subnet IDs

  tags = {
    Name = "my-db-subnet-group"
  }
}

resource "aws_db_instance" "mysql" {
  allocated_storage    = 20
  storage_type         = "gp2"
  engine               = "mysql"
  engine_version       = "8.0"
  instance_class       = "db.t2.micro"
  username             = "admin"
  password             = "your_password"  # Replace with a strong password
  parameter_group_name = "default.mysql8.0"
  db_subnet_group_name = aws_db_subnet_group.default.name  # Use the name from your DB subnet group
  vpc_security_group_ids = ["sg-02de1ef65a17895cf"]
  multi_az             = false
  publicly_accessible  = true
  skip_final_snapshot  = true  # Optional: Avoids creating a final snapshot on deletion

  tags = {
    Name = "mysql-instance"
  }
}
