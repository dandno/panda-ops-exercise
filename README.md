# panda-ops-exercise
### Assumpsions
1. Docker and docker-compose are already installed on you host
if not, install it according to following instructions:
[docker](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/)
2. You are using python version 2.7

### deployment-flow.py
Usage: ```new-flow.py [-h] -images_url IMAGES_URL -images_dir IMAGES_DIR
                   -health_check_url HEALTH_CHECK_URL```

- images_url - URL to images location tar.gz file (will be extracted to images_dir)
- images_dir - location to extract images_url
- health_check_url - container's healthcheck url
 
Example:
