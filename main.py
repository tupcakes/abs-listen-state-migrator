# import json
import argparse
from audiobookshelf import search_library, get_item_by_id, update_media_progress, get_media_progress, get_library_items, delete_media_progress


# Main script logic
# Initialize parser
parser = argparse.ArgumentParser()

# Adding arguments
parser.add_argument("-sapi", "--source_api_key", required=True, help="API Key for authorization for source")
parser.add_argument("-dapi", "--dest_api_key", required=True, help="API Key for authorization destination")
parser.add_argument("-surl", "--source_url", required=True, help="Source url (http://abs.example.com")
parser.add_argument("-durl", "--dest_url", required=True, help="Dest url (http://abs.example.com")
parser.add_argument("-slid", "--source_library_id", required=True, help="Source library ID")
parser.add_argument("-dlid", "--dest_library_id", required=True, help="Dest library ID")

# Read arguments from command line
args = parser.parse_args()

# Assign arguments to variables
source_api_key = args.source_api_key
dest_api_key = args.dest_api_key
source_url = args.source_url
dest_url = args.dest_url
source_library_id = args.source_library_id
dest_library_id = args.dest_library_id

if source_library_id == dest_library_id:
    print("Source and destination libraries can't be the same.")
    exit()

# Loop through all library items in given library.
for item in get_library_items(source_url, source_api_key, source_library_id)["results"]:
    # get the media progress for the current item.
    try:
        source_item_progress = get_media_progress(source_url, source_api_key, item["id"])
    except:
        continue

    # get item ASIN from source library
    # if there isn't an ASIN OR ISBN, skip the item and continue
    source_item = get_item_by_id(source_url, source_api_key, source_item_progress["libraryItemId"])

    book_asin = source_item["media"]["metadata"]["asin"]
    book_isbn = source_item["media"]["metadata"]["isbn"]
    if book_asin is None and book_isbn is None:
        print("No ASIN or ISBN for: " + source_item["id"] + " - " + source_item["media"]["metadata"]["title"])
        continue

    # get dest_item_id from destination library
    if book_asin is not None:
        search_results = search_library(dest_url, dest_api_key, dest_library_id, book_asin)
    elif book_isbn is not None:
        search_results = search_library(dest_url, dest_api_key, dest_library_id, book_isbn)
    else:
        # this condition should never be reached.
        print("PANIC: No book identifier. How the hell did I get here?")
        break

    dest_item_id = search_results["book"][0]["libraryItem"]["id"]
    print(dest_item_id + " - " + source_item["media"]["metadata"]["title"])

    # update dest mediaProgress for dest_item_id
    try:
        dest_item_progress = get_media_progress(dest_url, dest_api_key, dest_item_id)
        delete_media_progress(dest_url, dest_api_key, dest_item_progress["id"])
    except:
        print("No progress to delete.")
    update_media_progress(dest_url, dest_api_key, dest_item_id, source_item_progress)
