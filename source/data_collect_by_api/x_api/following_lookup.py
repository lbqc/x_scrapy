import requests
import os
import json

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")


def create_url(user_id=1717369046608523264):
    # Replace with user ID below
    user_id = 1717369046608523264
    return "https://api.twitter.com/2/users/{}/following".format(user_id)


def get_params():
    return {"user.fields": "username"}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FollowingLookupPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    url = create_url()
    params = get_params()
    json_response = connect_to_endpoint(url, params)
    print(json.dumps(json_response, indent=4, sort_keys=True))


def get_followings_by_userid(user_id, ):
    url = create_url(user_id)
    params = get_params()
    json_response = connect_to_endpoint(url, params)
    return json.dumps(json_response, indent=4, sort_keys=True)


if __name__ == "__main__":
    main()
