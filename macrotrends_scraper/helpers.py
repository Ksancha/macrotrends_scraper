import pandas as pd
from bs4 import BeautifulSoup


def get_dates(soup):
    dates = []
    for col in soup.find(id="columntablejqxgrid").contents[3:]:
        dates.append(col.text)
    return dates


def get_rows(soup):
    rows = []
    for row in soup.find(id="contenttablejqxgrid").contents:
        rows.append([x.text for x in row])
    return rows


def get_balance_sheet_df(html):

    soup = BeautifulSoup(html, 'html.parser')
    cols = get_dates(soup)
    rows = get_rows(soup)
    index_col = [x[0] for x in rows]
    values = [x[len(rows[0]) - len(cols):] for x in rows]
    # TODO: Convert values to floats and dates to datetimes
    df = pd.DataFrame(data=values, columns=cols, index=index_col)
    return df





