from youtubestats import YTstats

api_key_21='AIzaSyAUi6yKKl-KSqo08GMapC_aT1EI7GnNP0s'
API_KEY=api_key_21
python_engineer_id = 'UCbXgNpp0jedKWcQiULLbDTA'
channel_id = python_engineer_id

yt_PE = YTstats(API_KEY, python_engineer_id)

yt_PE.get_channel_statistics()
yt_PE.get_channel_video_data()
yt_PE.dump()
