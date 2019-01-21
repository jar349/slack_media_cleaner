Slack Media Cleaner
---
Simple script that uses the python Slack API to delete all uploaded images to free up room in your free Slack workspace

## How to run it
1. edit `config.yaml` and put your token in there
1. build the docker image: `docker build -t jar349/slack_media_cleaner:latest .`
1. create a container: `docker create --name slack_cleaner jar349/slack_media_cleaner:latest` 
1. start the container `docker start slack_cleaner`

from then on you can run it whenever you like by just:
`docker start slack_cleaner`

you can also see logs (if you care) by: `docker logs slack_cleaner`

### Considerations
It occurs to me that I shouldn't have gotten `slack_token` from a config file; that I should get it from the env so 
that it can be passed to the container via ``-env SLACK_TOKEN=xop-the-token`.  Maybe one day when I care enough?

