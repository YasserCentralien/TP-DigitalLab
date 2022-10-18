from dash import Dash, html, dcc
############################################################################################################################################

external_stylesheets = [{"href": "./assets/styles.css", "rel": "stylesheet"}]
app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.layout = html.Div(children=[
    # Header
    html.Div(
        children=[
            # Title
            html.Div(children=[
                html.H1(children="The impact of Covid 19 on the World Economy"),
                html.
                P(children=
                  "Comparing the evolution of Covid 19 and that of the global economy",
                  className="header__title")
            ]),
            html.Img(src="./assets/dash-new-logo.png",
                     className="header__logo")
        ],
        className="header"),
    # Content
    html.Div(children=[
        html.Div(children=[html.Img(src="./assets/Cumulative_cases.png",
                     className=""),html.Img(src="./assets/GPD.png",
                     className="")], className="right_plot column"),
        html.Div(children=[html.P(children="Interpretation",className='H2'),
                html.
                P(children=
                  " - As figure 1 shows, Gross Domestic Products per capita (GDP) acts as a metric for determining a country's economic output per each person living there.",
                  className="paragraphe"),html.
                P(children=
                  " - As figure 1 shows, GDP fallen in Japan and Italy compared to Brazil after COVID-19. India and China had the highest GDP growth rates.",
                  className="paragraphe"),
                html.
                P(children=
                  " - Figure 2 shows that Inflation growth rates in India and Brazil were high during the pandemic.",
                  className="paragraphe"),
                html.
                P(children=
                  " - Populations in Germany and Japan declined significantly after 2019 based on figure 3.",
                  className="paragraphe"),
                html.
                P(children=
                  " Conclusion : Based on our research and datasets, the Covid-2019 did not have a significant impact on the main economy indicator(GDP).",
                  className="paragraphe")], className="middle_plot column"),
        html.Div(children=[
            html.Img(src="./assets/inflation.png",
                     className=""),
            html.Img(src="./assets/population.png",
                     className="")
        ], className="right_plot column")
    ],                      
             className="content")
], className="container")

if __name__ == '__main__':
    app.run_server(debug=True)