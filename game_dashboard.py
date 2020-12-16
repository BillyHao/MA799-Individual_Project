import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

df = pd.read_csv('./data/game_new.csv', encoding="gbk")

platform_list = list(df['platform'].unique())
date_list = sorted(set([x for x in list(df['date']) if x != ""]))
genre_list = list(df['genre'].unique())
user_score_list = sorted(set([float(x) for x in list(df['user_socre'].unique()) if x != 'tbd']))
# print(min(user_score_list),max(user_score_list))
meta_score_list = sorted(set([int(x) for x in list(df['meta_socre'].unique()) if x != ""]))
# print(min(meta_score_list),max(meta_score_list))
rate_num_list = sorted(set([int(x) for x in list(df['rate_num'].dropna().unique())]))
# print(min(rate_num_list),max(rate_num_list))
# print(len(genre_list))
# print(date_list)
# print(type(df.head(10)),df)
# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=stylesheet)
# colors = dict(background = '#111111', text = '#7FDBFF')
server = app.server
colors = dict(background='#111111', text='#7FDBFF')

server = app.server

def generate_table(dataframe, ddf, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(10, len(dataframe)))
        ])
    ],
        # style="word-break:break-all;"
    ), dcc.Graph(
        id='example-graph',
        figure=dict(
            data=[{'x': list(ddf['title'][:min(len(ddf), 10)]), 'y': list(ddf["user_socre"])[:min(len(ddf), 10)],
                   'type': 'bar', 'name': 'user_score'}
                  ],
            layout=dict(title='User Socre')
        )
    ), \
           dcc.Graph(
               id='example-graph',
               figure=dict(
                   data=[
                       {'x': list(ddf['title'][:min(len(ddf), 10)]), 'y': list(ddf["meta_socre"])[:min(len(ddf), 10)],
                        'type': 'bar', 'name': 'meta_score', }],

                   layout=dict(title='Meta Score',
                               plot_bgcolor=colors['background'],
                               paper_bgcolor=colors['background'],
                               font={'color': colors['text'],

                                     }

                               ),

                   # marker=dict(colors="red"),

                   # yaxis={
                   #     # 'hoverformat': '.2%',
                   #     # 'showline': True,
                   #     # 'showgrid': True,
                   #     # 'side': 'right',
                   # }

               ),

           )


app.layout = html.Div(children=[
    html.H1('Help users choose video games',
            style=dict(textAlign='center', color=colors['text'])),
    html.H2('Produced by Quanlin Hao',
            style=dict(textAlign='center', color=colors['text'])),
   
    html.Label('genre'),
    dcc.Dropdown(
        options=[{"label": x, "value": x} for x in genre_list[:25]],
        # options=[{'label': 'aa', 'value': 'aa'},
        #          {'label': 'bb', 'value': 'bb'},
        #          {'label': 'cc', 'value': 'cc'}],
        value=genre_list,
        id="genre_id",
        multi=True
    ),
    # html.Label('—'*100),
    html.Label('platform'),
    dcc.Dropdown(
        options=[{"label": x, "value": x} for x in platform_list],
        # options=[{'label': 'aa', 'value': 'aa'},
        #          {'label': 'bb', 'value': 'bb'},
        #          {'label': 'cc', 'value': 'cc'}],
        value=platform_list,
        id="platform_id",
        multi=True

    ),
    # html.Label('—'*100),
    html.Label('release'),
    dcc.Dropdown(
        options=[{"label": x, "value": x} for x in date_list],
        # options=[{'label': 'aa', 'value': 'aa'},
        #          {'label': 'bb', 'value': 'bb'},
        #          {'label': 'cc', 'value': 'cc'}],
        value=date_list,
        id="release_id",
        multi=True
    ),

    html.Label('game name'),
    dcc.Input(value='',
              type='text',
              id="key_id",

              ),
    # html.Label('—'*100),
    html.Label('user score'),
    dcc.Slider(
        id="user_score_id",
        # muti=True,
        # multi=True,
        min=0, max=10, value=10,
        marks={
            0: "min:0",
            5: "mean:5",
            10: "max:10",

        }),
    # html.Label('—'*100),
    html.Label('meta score'),
    dcc.Slider(
        id="meta_score_id",
        # muti=True,
        min=meta_score_list[0], max=meta_score_list[-1], value=meta_score_list[-1],
        marks={
            
            meta_score_list[0]: "min:{}".format(meta_score_list[0]),
            meta_score_list[int(len(meta_score_list) / 2)]: "mean:{}".format(
                meta_score_list[int(len(meta_score_list) / 2)]),
            meta_score_list[-1]: "max:{}".format(meta_score_list[-1]),
        }),
    # html.Label('—'*100),
    # html.Label('—'*100),
    # html.Label('—'*100),
    # html.Label('—'*100),
    html.Label('rate_num'),
    dcc.Slider(
        id="rate_num_id",
        # muti=True,
        min=4, max=17732, value=rate_num_list[-1],
        
        marks={
            rate_num_list[0]: "min:{}".format(rate_num_list[0]),
            8864: "mean:8864",
            rate_num_list[-1]: "max:{}".format(rate_num_list[-1])
        }
        #
        #        }
    ),

    html.Div(id="df_div"),


],
    style={'columnCount': 2}
)


# Update the table
@app.callback(
    Output(component_id='df_div', component_property='children'),
    [
        Input(component_id='genre_id', component_property='value'),
        Input(component_id='release_id', component_property='value'),
        Input(component_id='platform_id', component_property='value'),
        Input(component_id='key_id', component_property='value'),
        Input(component_id='user_score_id', component_property='value'),
        Input(component_id='meta_score_id', component_property='value'),
        Input(component_id='rate_num_id', component_property='value'),
    ]
)
def update_table(genre_id, release_id, platform_id, key_id, user_score_id, meta_score_id, rate_num_id):
    # print('platform_id:',platform_id)
    # print("genre:",genre_id)
    # print("release_id:",release_id)
    # print("key_id:",key_id)
    # print("user_score_id",user_score_id)
    # print("meta",meta_score_id)
    # print("rate",rate_num_id)
    # x = df[df.Fruit.isin(fruits_to_display)].sort_values(sort_by, ascending=(sort_by != "Amount"))
    # df[df.platform.isin(platform_id)]
    # print(df[df['platform'].isin([platform_id])])
    # x=df[df['platform'].isin([platform_id])][['title','summary']]
    if key_id == "":
        x = df[df['genre'].isin(genre_id)][df['platform'].isin(platform_id)][df['date'].isin(release_id)] \
            [['title', "platform", "date", 'summary']]
        y = df[df['genre'].isin(genre_id)][df['platform'].isin(platform_id)][df['date'].isin(release_id)]
        # print(type(x['summary']))
        # x['summary'] = pd.Series(["platform:" + x + "//" for x in y['platform']])[:len(y['summary'])] + pd.Series(
        #     ["date:" + x + "___" * 17 for x in y['date'].map(str)])[:len(y['summary'])] + \
        #                y['summary']
        # x['summary']=y[y.columns[1:]]
        print(x)
        # [df['user_socre'].isin([user_score_id])] \
        # [df['meta_socre'].isin([meta_score_id])] \
        # [df['rate_num'].isin([rate_num_id])] \

    else:
        x = df[df['title'].isin([key_id])] \
            [['title', "platform", "date", 'summary']]

        y = df[df['title'].isin([key_id])][0:1]
        # y["title"]=y["title"]+pd.Series([x for x in range(len(y["title"]))])
        # x['summary'] = pd.Series(["platform:" + x + "//" for x in y['platform']])[:len(y['summary'])] + pd.Series(
        #     ["date:" + x + "___" * 17 for x in y['date'].map(str)])[:len(y['summary'])] + \
        #                y['summary']
    if user_score_id != 10:
        x = df[df['user_socre'].isin([user_score_id])][['title', "platform", "date", 'summary']]
        y = df[df['user_socre'].isin([user_score_id])]
        # x['summary'] = pd.Series(["platform:" + x for x in y['platform']])[:len(y['summary'])] + pd.Series(
        #     ["date:" + x  for x in y['date'].map(str)])[:len(y['summary'])] + \
        #                y['summary']
    if meta_score_id != meta_score_list[-1]:
        x = df[df['meta_socre'].isin([meta_score_id])][['title', "platform", "date", 'summary']]
        y = df[df['meta_socre'].isin([meta_score_id])]
        # x['summary'] = pd.Series(["platform:" + x + "//" for x in y['platform']])[:len(y['summary'])] + pd.Series(
        #     ["date:" + x + "___" * 17 for x in y['date'].map(str)])[:len(y['summary'])] + \
        #                y['summary']
    if rate_num_id != rate_num_list[-1]:
        x = df[df['rate_num'].isin([rate_num_id])][['title', "platform", "date", 'summary']]
        y = df[df['rate_num'].isin([rate_num_id])]
        # x['summary'] = pd.Series(["platform:" + x + "//" for x in y['platform']])[:len(y['summary'])] + pd.Series(
        #     ["date:" + x + "___" * 17 for x in y['date'].map(str)])[:len(y['summary'])] + \
        #                y['summary']

    # print(x)
    # print(df)
    return generate_table(x, y, max_rows=10)


# Update the bar
# @app.callback(
#     Output(component_id='example-graph', component_property='children'),
#     [Input(component_id='fruit_select_checklist', component_property='value')]
# )
# def update_slider(fruits_to_display):
#     x = df[df.Fruit.isin(fruits_to_display)]
#     return min(10, len(x))


if __name__ == '__main__':
    # print(df)
    app.run_server(
        port=5001
        , debug=True)
