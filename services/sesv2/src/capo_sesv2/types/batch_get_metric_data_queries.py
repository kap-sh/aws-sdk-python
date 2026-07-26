"""Generated from Smithy shape ``com.amazonaws.sesv2#BatchGetMetricDataQueries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.batch_get_metric_data_query

BatchGetMetricDataQueries: TypeAlias = list[
    "capo_sesv2.types.batch_get_metric_data_query.BatchGetMetricDataQuery"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetMetricDataQueries) -> list:
    import capo_sesv2.types.batch_get_metric_data_query

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.batch_get_metric_data_query.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetMetricDataQueries:
    import capo_sesv2.types.batch_get_metric_data_query

    out: BatchGetMetricDataQueries = []
    for item in data:
        out.append(capo_sesv2.types.batch_get_metric_data_query.deserialize_json(item))
    return out
