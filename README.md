### Cicle CI:
[![CircleCI](https://circleci.com/gh/tintrandn/udacity-p5-capstone/tree/main.svg?style=svg)](https://app.circleci.com/pipelines/github/tintrandn/udacity-p5-capstone?branch=main)

# Udacity Capstone Project
In this project you will apply the skills and knowledge which were developed throughout the Cloud DevOps Nanodegree program. These include:

* Working in AWS
* Using Circle CI to implement Continuous Integration and Continuous Deployment
* Building pipelines
* Working with CloudFormation to deploy clusters/infrastructure
* Building Docker containers in pipelines
* Building Kubernetes clusters

# Set up Circle CI
1. Create new git repo and clone it
2. Set up circle ci for this project
3. Add env variables to circle ci
* `AWS_DEFAULT_REGION`
* `AWS_ACCESS_KEY_ID`
* `AWS_SECRET_ACCESS_KEY`
* `AWS_DEFAULT_REGION`
* `DOCKER_HUB_PASSWORD`
* `DOCKER_HUB_USERNAME`

## Run Steps For Cloud Deployment
* Create a DockerHub public repository
* Run chmod 700 for each Shell scrip in `./scripts` folder
* Run `./scripts/create-stack.sh capstone-network cloudformation/network.yml cloudformation/network-params.json` to create VPC infrastructure
* Run `./scripts/create-stack.sh capstone-eks-cluster cloudformation/aws-eks-cluster.yml cloudformation/aws-eks-cluster-params.json` to create EKS cluster
* Run `./scripts/create-stack.sh capstone-eks-nodegroup cloudformation/aws-eks-nodegroup.yml cloudformation/aws-eks-nodegroup-params.json` to create EKS nodes group

## Update config for circle ci
* Add jobs to trigger circle ci pipline
* Done!