from youtubestats import YTstats
from analyseData import *

api_key_21='******'
API_KEY=api_key_21
python_engineer_id = 'UCbXgNpp0jedKWcQiULLbDTA'
channel_id = python_engineer_id

cn=YouTubeAnalysis(API_KEY, python_engineer_id)
print(cn.get_view_statistics())
