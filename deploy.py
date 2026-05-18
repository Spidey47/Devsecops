import paramiko


ECR_REPO = "585008083177.dkr.ecr.us-west-2.amazonaws.com/devsecops"
REGION = "us-west-2"
EC2_HOST = "34.220.207.164"
EC2_USER = "ec2-user"
KEY_PATH = "C:/Users/Asus/OneDrive/Documents/DevOps/Devops mine/Terraform/devsecops-key.pem"


def deploy_to_ec2():
    print("Connecting to EC2...")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(EC2_HOST, username=EC2_USER, key_filename=KEY_PATH)

    print("Deploying latest image from ECR...")

    commands = [
        f"aws ecr get-login-password --region {REGION} | docker login --username AWS --password-stdin {ECR_REPO}",
        f"docker pull {ECR_REPO}:latest",
        "docker stop devsecops || true",
        "docker rm devsecops || true",
        f"docker run -d --restart always -p 8000:8000 --name devsecops {ECR_REPO}:latest"
    ]

    for cmd in commands:
        print(f"\n Running: {cmd}")
        stdin, stdout, stderr = ssh.exec_command(cmd)
        print(stdout.read().decode())
        print(stderr.read().decode())

    ssh.close()
    print("\n Deployment Complete!")


if __name__ == "__main__":
    deploy_to_ec2()
