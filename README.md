# BOTus-Twitter
> BOTus Twitter Bot. Shitpostings and other stuff.

## Developing

### Built With
* [Flask](http://flask.pocoo.org/)

### Prerequisites
* [Docker Community Edition](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/)
* Create your own dummy Twitter account and apply for developer access using that account

### Setting up the development environment
```sh
git clone git@github.com:Good-Stone/BOTus-Twitter.git
cd BOTus-Twitter/
cp .env.example .env
```

### Modify the Twitter configurations (after applying for the developer access) on the .env file

### Running the application in development mode
```sh
docker-compose up
```

Open `localhost:5000` in your browser to verify that the web server is up.
