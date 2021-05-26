import json
import pandas as pd

def get_complete_video_statistics(file):
    df_kn=get_basic_statistics(file)
    vd_knldg= get_video_dataframe(df_kn)

    return vd_knldg


def get_basic_statistics_both(file):
    with open(file, 'r') as f:
        data = json.load(f)

    channel_id, stats = data.popitem()
    channel_stats = stats['channel_statistics']
    video_stats = stats['video_data']

    # print(('channel_name : '),file[:-5].replace('_',' '))
    # print('*****************************')
    ser_cs = pd.Series(channel_stats)
    # print(ser_cs)

    df_pe = pd.DataFrame(video_stats).transpose()

    return df_pe, ser_cs
def get_basic_statistics(file):
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

def get_concise_video_statistics(file):
    df_kn, ser_cs= get_basic_statistics_both(file)
    vd_knldg= get_video_dataframe(df_kn)

    kv=vd_knldg[['title','viewCount']].sort_values(by='viewCount', ascending=False)
    pp=kv.describe()/1000
    print("********************")
    print('')
    print(('channel_name : '),file[:-5].replace('_',' '))
    print('*****************************')
    pp=pp.rename(columns={'viewCount':'total view in thousand '})
    pp.loc['subscribers']=int(ser_cs['subscriberCount'])/1000
    return pp


def get_video_dataframe(df_pe):
    main_columns = ['categoryId', 'channelTitle', 'title', 'viewCount', 'duration', 'commentCount',
                    'contentRating', 'definition', 'description',
                    'dimension', 'dislikeCount', 'favoriteCount',
                    'licensedContent', 'likeCount', 'localized',
                    'publishedAt', 'tags', 'caption']

    dfm = df_pe[main_columns]

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


