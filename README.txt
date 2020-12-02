
This file describes simple containers to run data science programs. The continers can
be run with or without
    * host directory bind-mounted in the container
    * A Flask web server running for

Dockerfile.runbash is outfitted with python, numpy, scipy, etc. and executes a bash shell as the CMD.

It is intended to be run with or without a shared drive on the host.

    docker build -t testcontainer .

To build one with an explicit version, just add the tag

    docker build -t testcontainer:v1 .

Executing the "docker run" command below will run the container and leave you in an interactive bash shell.
There is a file called setup.sh that has been copied to your container so sourcing this should give a way
to set environment variables, etc.

    docker run --name=tc1 -v /home/petercoates/Desktop/docker-shell/shared:/var/log/tc1  -it testcontainer:latest

In this case, it will be the directory in the clause to the left of the : on the host, and /var/log/tc1 on the container.
You can adjust either to suit.


To get an environment with no shared data on the host drop the "-v"

    docker run -it testcontainer:latest

If you run the container in the background or from another shell you can still get a bash shell on it

    docker exec -it <container-name or ID> bas

Note that this is a DIFFERENT bash shell. You won't be able to see the environment you may have sourced from
elsewhere, e.g., from a bash shell you have opened.

You won't be able to build if a container of the same name and version exists, even if it is stopped.
To rememdy this, the following should suffice.  The first is only necessary if you've run it in the background.
    docker kill testcontainer
    docker rm <container:version> will remove the container so you can build again
    docker container prune  will remove all unsued containers including the one you care about

You can, however, butild a container of a different version no matter how many other containers are running, e.g.,

    docker build -t testcontainer:v1 .
    docker build -t testcontainer:v2 .

Note, you have to differentiate when you run.

We assume you have the following files. The dockerfile is just a renamed copy of Dockerfile.runbash

    Dockerfile                      The basic makefile for your container
    install_packages.sh             A script to upgrade, install packages, run pip3 install, etc
    requirements.txt                Currently empty but some applications will want it
    setup.sh                        A file to source for the environment variables your code expects.

And have create directory shared in the right place to match your run command.

Note the Docker images tend to be stripped down. E.g., the python container this one is based on didn't include vim.

You may need to add certain capabilities to the install_packages script with apt-get.  (plain apt may not find the packages to install)



