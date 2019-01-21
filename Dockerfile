FROM python:2.7
LABEL maintainer="John Ruiz <jruiz@johnruiz.com>"

RUN pip install pipenv
COPY . /usr/local/slack_media_cleaner

RUN chmod +x /usr/local/slack_media_cleaner/entrypoint.sh
ENTRYPOINT [ /usr/local/slack_media_cleaner/entrypoint.sh ]
