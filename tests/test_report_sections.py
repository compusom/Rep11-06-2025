import pandas as pd
from datetime import datetime
from data_processing.report_sections import _generar_tabla_bitacora_top_ads


def test_top_ads_audience_lines(capsys):
    df = pd.DataFrame({
        'date': pd.to_datetime(['2024-06-01','2024-06-02']),
        'Campaign': ['Camp','Camp'],
        'AdSet': ['Set','Set'],
        'Anuncio': ['Ad1','Ad1'],
        'spend': [10, 20],
        'impr': [100, 200],
        'reach': [80, 150],
        'purchases': [1, 2],
        'visits': [10, 20],
        'value': [50, 120],
        'clicks': [5, 10],
        'clicks_out': [1, 2],
        'rv3': [0, 0],
        'rv25': [1, 2],
        'rv75': [0, 1],
        'rv100': [0, 1],
        'rtime': [4, 5],
        'url_final': ['https://test.com','https://test.com'],
        'bid': [5,5],
        'thruplays': [3,4],
        'Públicos In': ['Inc1', 'Inc2'],
        'Públicos Ex': ['Exc1', 'Exc2'],
    })
    periods = [
        (datetime(2024,6,1), datetime(2024,6,2), 'Semana actual'),
        (datetime(2024,5,25), datetime(2024,5,31), '1ª semana anterior'),
        (datetime(2024,5,18), datetime(2024,5,24), '2ª semana anterior'),
    ]
    active = pd.DataFrame({
        'Campaign': ['Camp'],
        'AdSet': ['Set'],
        'Anuncio': ['Ad1'],
        'Días_Activo_Total': [2]
    })
    logs = []
    _generar_tabla_bitacora_top_ads(df, periods, active, logs.append, '$', top_n=1)
    output = "\n".join(logs)
    assert 'Públicos Incluidos:' in output
    assert 'Inc1' in output and 'Inc2' in output
    assert 'Públicos Excluidos:' in output
    assert 'Exc1' in output and 'Exc2' in output
    assert 'URL FINAL:' in output and 'https://test.com' in output
    assert 'Puja:' in output and '$5,00' in output
    assert 'ThruPlays:' in output and '7' in output
    assert 'Reproducciones de video 25%' in output

def test_top_ads_static_no_video_lines(capsys):
    df = pd.DataFrame({
        'date': pd.to_datetime(['2024-06-01']),
        'Campaign': ['Camp'],
        'AdSet': ['Set'],
        'Anuncio': ['Ad2'],
        'spend': [5],
        'impr': [50],
        'reach': [40],
        'purchases': [0],
        'visits': [5],
        'value': [0],
        'clicks': [2],
        'clicks_out': [1],
        'rv3': [0],
        'rv25': [0],
        'rv75': [0],
        'rv100': [0],
        'rtime': [0],
        'url_final': ['https://test.com'],
        'bid': [2],
        'thruplays': [0],
        'Públicos In': ['aud'],
        'Públicos Ex': ['ex'],
    })
    periods = [
        (datetime(2024,6,1), datetime(2024,6,1), 'Semana actual'),
        (datetime(2024,5,25), datetime(2024,5,31), '1ª semana anterior'),
        (datetime(2024,5,18), datetime(2024,5,24), '2ª semana anterior'),
    ]
    active = pd.DataFrame({
        'Campaign': ['Camp'],
        'AdSet': ['Set'],
        'Anuncio': ['Ad2'],
        'Días_Activo_Total': [1]
    })
    logs = []
    _generar_tabla_bitacora_top_ads(df, periods, active, logs.append, '$', top_n=1)
    output = "\n".join(logs)
    assert 'Reproducciones de video 25%' not in output
