# QHerde

This is a very minimalistic Python app that will be used in our RKE demo. It has a single endpoint that returns a JSON response that has ADSExchange data. This data is used within the single template (index.html) to display aircrafts on a map. This is updated every 5 seconds.

The application expects the following environment variables to be set:

- rapidapi_key: The key to access the ADSExchange API
- rapidapi_host: The host to access the ADSExchange API

Both values are available on the RapidAPI website.
