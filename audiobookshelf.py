from api_helper import api_request, api_patch, api_delete

def get_user(url, api_key, user_id):
    url = f"{url}/api/users/{user_id}"
    headers = {
        "accept": "application/json",
        "authorization": api_key
    }
    return api_request("GET", url, headers)

def search_library(url, api_key,library_id,  search_term):
    url = f"{url}/api/libraries/{library_id}/search?q={search_term}"
    headers = {
        "accept": "application/json",
        "authorization": api_key
    }
    return api_request("GET", url, headers)

def get_item_by_id(url, api_key, item_id):
    url = f"{url}/api/items/{item_id}"
    headers = {
        "accept": "application/json",
        "authorization": api_key
    }
    return api_request("GET", url, headers)

def get_media_progress(url, api_key, item_id):
    url = f"{url}/api/me/progress/{item_id}"
    headers = {
        "accept": "application/json",
        "authorization": api_key
    }
    return api_request("GET", url, headers)

def update_media_progress(url, api_key, item_id, media_progress_item):
    url = f"{url}/api/me/progress/{item_id}"
    headers = {
        "accept": "application/json",
        "authorization": api_key
    }

    if media_progress_item["isFinished"] is False:
        payload = {
            "currentTime": media_progress_item["currentTime"],
            "duration": media_progress_item["duration"],
            "progress": media_progress_item["progress"],
            "startedAt": media_progress_item["startedAt"]
        }
    elif media_progress_item["isFinished"] is True:
        payload = {
            'currentTime': media_progress_item["duration"],
            'duration': media_progress_item["duration"],
            'isFinished': media_progress_item["isFinished"],
            'finishedAt': media_progress_item["finishedAt"],
            'startedAt': media_progress_item["startedAt"]
        }
    else:
        return 1

    return api_patch(url, headers, payload)


def delete_media_progress(url, api_key, item_id):
    url = f"{url}/api/me/progress/{item_id}"
    headers = {
        "accept": "application/json",
        "authorization": api_key
    }
    return api_delete(url, headers)

def get_library_items(url, api_key, library_id):
    url = f"{url}/api/libraries/{library_id}/items"
    headers = {
        "accept": "application/json",
        "authorization": api_key
    }
    return api_request("GET", url, headers)
