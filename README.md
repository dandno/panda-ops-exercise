# panda-ops-exercise

### Assumpsions
1. Docker and docker-compose are already installed on you host if not, install it according to following instructions: docker and docker-compose
2. You are using python version 2.7

### deployment-flow.py


Usage: ```new-flow.py [-h] -images_url IMAGES_URL -images_dir IMAGES_DIR -health_check_url HEALTH_CHECK_URL```

- images_url - URL to images location tar.gz file (will be extracted to images_dir)
- images_dir - location to extract images_url
- health_check_url - container's healthcheck url

Description: 
1.	Download tar file from $images_url
2.	Extract the tar file to $images_dir
3.	Run docker-compose up (against the docker-compose.yml in the home directory)
4.	Check return code of $health_check_url


Example: ```deployment-flow.py -images_url https://s3.eu-central-1.amazonaws.com/devops-exercise/pandapics.tar.gz -images_dir public/images -health_check_url http://localhost:3000```
