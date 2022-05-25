# set the base container image
FROM python:3.6-alpine

LABEL maintainer="joseph"

# creating a new user
RUN adduser -D joseph

#setting the workdir to be the home of the new user
WORKDIR /home/joseph

# RUN ls -lrt
# copy requirements.txt from the project file to the home dir
COPY requirements.txt ./requirements.txt

# create a virtual environment
RUN python3 -m venv venv

# enter venv
RUN source venv/bin/activate

# install requirements
RUN pip3 install -r requirements.txt

# copy app folder to working dir
COPY api api
COPY migrations migrations
COPY models models
COPY start.sh start.sh
COPY Procfile Procfile

# copy run.py and config.py and boot.sh to working dir
# COPY migrations models start.sh ./

# set permission of sh file
RUN chmod +x start.sh

# RUN pwd; ls -lrt

ENV FLASK_APP api/v1/app.py
ENV DB_URI $DB_URI

# RUN flask db migrate
# RUN flask db upgrade
RUN chown -R joseph:joseph ./
USER joseph

EXPOSE 5000
# ENTRYPOINT ["./start.sh"]

RUN ./start.sh

RUN echo $DB_URI
# to run the application vanila flask
# CMD [ "flask", "run", "--host=0.0.0.0"]

# CMD ["gunicorn", "--bind", "0.0.0.0:40569", "api.v1.app:app"]
CMD ["gunicorn", "api.v1.app:app"]