# Sample docker for the SHINY-ICARUS Challenge

This sample docker performs a threshold over the images on an input path.
We will walk you through all the steps you will need to follow in order to prepare your docker container and submit it to the challenge.


# 0. Corroborate that your method complies with all the requirements

1. Be fully automatic and deterministic (make sure there are no random seeds required for prediction).
1. Run on a system with 60GB RAM and a GTX 3060 12GB.
1. Maximum docker size 20GB.
1. File prediction should not take more than 1 hour per case.


# 1. Create a Synapse Project for submission

Firstly, you will need to create a Synapse Project that will allow you to participate with your submission.
You can do this easily by signing in to your Synapse account, going to the Projects tab to the left and creating a new project.
This project will have an associated Synapse ID (`syn<number>`).


# 2. Install docker

You will need to install docker on your computer to be able to build and upload it to your Synapse Project.
To do that, you can follow the [instructions](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository) on the official docker webpage.

# 3. Prepare your docker

## Dockerfile
Here you'll indicate how to run your segmentation code. This includes:
1. The programming language and version your code is written on
1. Install commands for all the required libraries
1. Add command to include the required repository files (with `ADD . .` the complete repository will be added)
1. Run command to execute your code

You can read the complete [Dockerfile reference](https://docs.docker.com/engine/reference/builder/) on the official docker webpage. 

## Paths to volumes

Your segmentation method will need to read and write files from the following folders:

`in_path = "/input"`

`out_path = "/output"`

# 4. Add docker to your Synapse project

Once your docker container is ready, you will have to run a few commands locally. Make sure to execute them on the directory where your docker files are.

First, log in to your Synapse account:

`docker login -u <YourUsername> -p <YourPassword> docker.synapse.org`

Then, build your docker through the Synapse services

`docker build -t docker.synapse.org/syn<ProjectNumber>/<NameYourDocker> .`

Finally, push your docker to the Synapse Project

`docker push docker.synapse.org/syn<ProjectNumber>/<NameYourDocker>`

# 5. Submit your docker

Go to the Docker tab on your Synapse Project webpage. There, you will see the docker file you just pushed.

Select it and click on Docker Repository Tools.

Select Submit to Challenge.

Here, you will need to indicate which challenge you're submitting to. You can also give a name to your submission (recommended, since this makes it easier to find the logs associated to your submission).

Then, you can indicate whether you're submitting as a team or as an individual. If you're submitting as a team, remember to first Register your team on the challenge webpage.

Once you confirm, the pipeline will run. You will receive an email indicating if it ran successfully and a link where you will be able to see the logs of the execution.

If the docker execution ran without problems, you see the evaluation result over one random train case. This will allow you to corroborate that the model runs correctly over one (or more) cases.