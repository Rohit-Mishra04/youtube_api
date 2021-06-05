from analyticsUtil import *
from youtubestats import YTstats

class YouTubeAnalysis(YTstats):

    def __init__(self, api_key, channel_id):
        super().__init__(api_key, channel_id)
        self.get_channel_statistics()
        self.get_channel_video_data()
        self.dump()

        #

    def get_main_video_columns_df(self):
        main_columns = ['categoryId', 'channelTitle', 'title', 'viewCount', 'duration', 'commentCount',
                        'contentRating', 'definition', 'description',
                        'dimension', 'dislikeCount', 'favoriteCount',
                        'licensedContent', 'likeCount', 'localized',
                        'publishedAt', 'tags', 'caption']

        def get_basic_statistics(file):
            #
            with open(file, 'r') as f:
                data = json.load(f)

            channel_id, stats = data.popitem()
            channel_stats = stats['channel_statistics']
            video_stats = stats['video_data']

            print(('channel_name : '), file[:-5].replace('_', ' '))
            print('*****************************')
            print(pd.Series(channel_stats))

            df_pe = pd.DataFrame(video_stats).transpose()

            return df_pe

        dfm = get_basic_statistics(self.channel_file_name)

        dfm = dfm[main_columns]

        dfm['title'] = dfm.localized.apply(lambda x: x['title'])
        dfm['description'] = dfm.localized.apply(lambda x: x['description'])

        dfm = dfm.drop(columns='localized')

        # dfm[dfm.tags.isna()]['tags']=[]
        dfm['tags'] = dfm['tags'].fillna('DELETE').apply(lambda x: [] if x == 'DELETE' else x)

        dfm['tag_count'] = dfm.tags.apply(lambda x: len(x))

        dfm['viewCount'] = dfm.viewCount.apply(lambda x: int(x))
        dfm['dislikeCount'] = dfm.dislikeCount.apply(lambda x: int(x))
        dfm['likeCount'] = dfm.likeCount.apply(lambda x: int(x))
        dfm['commentCount'] = dfm.commentCount.apply(lambda x: int(x))
        dfm['favoriteCount'] = dfm.favoriteCount.apply(lambda x: int(x))

        return dfm

    def get_view_statistics(self):
        vd_knldg = self.get_video_dataframe()

        kv = vd_knldg[['title', 'viewCount']].sort_values(by='viewCount', ascending=False)
        pp = kv.describe() / 1000
        print("********************")
        print('')
        print(('channel_name : '), self.channel_file_name[:-5].replace('_', ' '))
        print('*****************************')
        pp = pp.rename(columns={'viewCount': 'total view in thousand '})
        #pp.loc['subscribers'] = int(ser_cs['subscriberCount']) / 1000
        return pp








