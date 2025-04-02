import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> list[int]:
    x = []
    rows = players.shape[0]
    columns = players.shape[1]
    x.extend([rows,columns])

    return x
