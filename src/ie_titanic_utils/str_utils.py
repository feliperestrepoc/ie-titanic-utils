import pandas as pd


# ie-titanic-utils
def extract_title(name):
    fragments = name.split(".")
    title = fragments[0]
    return title
