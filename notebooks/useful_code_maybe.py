

from typing import List

def change_currency(
    data: pd.DataFrame, currency_cols: List[str], country_col: str, countries: List[str], 
    denominations: List[str], target_currency: str
) -> pd.DataFrame:
    for col in currency_cols:
        for country, curr in zip(countries, denominations):
            condition = (data[country_col] == country)
            data.loc[condition, col] = data.loc[condition, col].apply(lambda x: round(c.convert(x, curr, target_currency), 2) if x is not np.nan else np.nan)
    
    return data



%%time

new_prices = defaultdict(dask.dataframe.Series)

for col in curr_cols:
    new_currs = []
    new_condition = []
    for country, curr in zip(countries, currencies):
        condition = (ddf16['country'] == country)
        new_currs.append(ddf16.loc[condition, col].apply(lambda x: round(c.convert(amount=x, currency=curr, new_currency='USD'), 2), meta=(col, 'float32')).astype(np.float32))
        new_condition.append(condition)
    new_prices[col] = ddf16[col].where(~new_condition[0], new_currs[0]).where(~new_condition[1], new_currs[1]).where(~new_condition[2], new_currs[2])
    
    
    %%time

new_prices = defaultdict(dask.dataframe.Series)

for country in countries:
    condition = (ddf16['country'] == country)
    for col in curr_cols:
        new_currs = ddf16.loc[condition, col]
        for curr in currencies:
            new_currs2 = new_currs.apply(lambda x: round(c.convert(amount=x, currency=curr, new_currency='USD'), 2), meta=(col, 'float32')).astype(np.float32)
    new_prices[col] = ddf16[col].where(~condition, new_currs2)

ddf17 = (ddf16.drop(list(new_prices.keys()), axis=1)
#               .assign(**new_prices)
        )
ddf18 = ddf17.assign(**new_prices)
ddf18.head()