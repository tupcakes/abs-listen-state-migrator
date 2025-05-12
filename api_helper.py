import requests

def api_request(method, url, headers, payload=None):
    """Generic API request handler."""
    response = requests.request(method, url, headers=headers, data=payload)
    response.raise_for_status()
    return response.json()

def api_patch(url, headers, payload=None):
    """Generic API patch handler."""
    response = requests.patch(url, headers=headers, data=payload)
    return response

def api_delete(url, headers):
    """Generic API delete handler."""
    response = requests.delete(url, headers=headers)
    return response
