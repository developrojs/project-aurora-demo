# project-aurora-demo

## Set up and Run demo

This is being tested on both Linux(Ubuntu 22.04) and Windows.  From a terminal window:

```
# git clone https://github.com/developrojs/project-aurora-demo.git

# cd projecy-aurora-demo

# pip install -r requirements.txt

# python main.py  
```

The demo is configured with a [Yelp Fusion client](https://docs.developer.yelp.com/docs/fusion-intro), where a [API key](https://docs.developer.yelp.com/docs/fusion-authentication) needs to be created and there are two ways the key can be passed to the demo program.

### .env file

At the directory where the program is being run, create a `.env` file that contains the key value pair

```
# cat .env
ENV_YELP_FUSION_APIKEY="api key"
```

### environment variable

Here uses Linux as an example, run the following at the shell session where the program is to be run:

```
export ENV_YELP_FUSION_APIKEY="api key"
```

or

```
ENV_YELP_FUSION_APIKEY="api key" python main.py
```

