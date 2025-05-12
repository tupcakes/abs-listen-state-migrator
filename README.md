# abs-listen-state-migrator
This python script will assist with migrating mediaProgress for an existing user in [Audiobookshelf](https://audiobookshelf.org).

I wrote this, admittedly shitty, script because I wanted to change my folder structure for my media, but found that audiobookshelf REALLY doesn't want you to do that. The script requires that either ASIN or ISBN be populated for the books that you want to sync listen state for (I had to have something to consistant key to between seperate libraries or even abs servers, and those seemed like the best option).

It should be noted that this only performs a limited migration of mediaProgress. It does NOT migrate listen stats. It does however migrate the following fields:
- currentTime
- duration
- isFinished
- finishedAt
- startedAt

## Options
```
-h, --help            show this help message and exit
-sapi, --source_api_key SOURCE_API_KEY
                      API Key for authorization for source
-dapi, --dest_api_key DEST_API_KEY
                      API Key for authorization destination
-surl, --source_url SOURCE_URL
                      Source url (http://abs.example.com
-durl, --dest_url DEST_URL
                      Dest url (http://abs.example.com
-slid, --source_library_id SOURCE_LIBRARY_ID
                      Source library ID
-dlid, --dest_library_id DEST_LIBRARY_ID
                      Dest library ID
```

## Example
```
python main.py \
--source_api_key "Bearer exJhbGciOiJI6IkpXVCJ9.eyJ1c2Vyi5NDEyODc4fQ.ZraBFohS4Tg39NszY" \
--dest_api_key "Bearer exJhbGciOiJI6IkpXVCJ9.879as8d7f9sdf79asf80sdf987dsf9s9df7898" \
--source_url "https://source-abs.example.net" \
--dest_url "https://destination-abs.example.net" \
--source_library_id "lib_c1u6t4p45c35rf0nzd" \
--dest_library_id "lib_8as6df87s6df87sd6f"
```
