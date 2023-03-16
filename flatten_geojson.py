import pandas as pd
def flatten_geojson(parent):
    '''
    Returns a DataFrame containing the properties from the supplied geojson dictionary structure.
    The hierarchy of object properties in the input is converted to a flattened representation comprising one row per item.
    '''

    #
    # convenience for Plotly Express chloropleth_mapbox:
    #
    objectid = 0
    for child in parent['features']:
        child['properties'].update({'id':objectid})
        child['id'] = objectid
        objectid += 1

    #
    # flatten properties to a data frame:
    #
    child_properties = [child['properties'] for child in parent['features']]
    df_child_properties = pd.DataFrame.from_dict(child_properties) 
    return df_child_properties