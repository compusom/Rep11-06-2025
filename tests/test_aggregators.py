import pandas as pd
from queue import SimpleQueue
from data_processing.aggregators import _agregar_datos_diarios


def test_agregar_diarios_includes_extra_fields():
    df = pd.DataFrame({
        'date': pd.to_datetime(['2024-06-01', '2024-06-01']),
        'Campaign': ['Camp', 'Camp'],
        'AdSet': ['Set', 'Set'],
        'Anuncio': ['Ad', 'Ad'],
        'spend': [10, 20],
        'impr': [100, 200],
        'reach': [50, 100],
        'value': [40, 80],
        'purchases': [1, 2],
        'clicks': [10, 20],
        'puja': [1.0, 1.5],
        'url_final': ['https://a.com', 'https://a.com/page'],
        'interacciones': [5, 6],
        'comentarios': [1, 2],
    })

    q = SimpleQueue()
    result = _agregar_datos_diarios(df, q)
    assert 'puja' in result.columns
    assert 'url_final' in result.columns
    assert 'interacciones' in result.columns
    assert 'comentarios' in result.columns

    row = result.iloc[0]
    assert row['puja'] == 1.25
    assert row['interacciones'] == 11
    assert row['comentarios'] == 3
    assert 'https://a.com' in row['url_final']
