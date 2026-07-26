"""Generated from Smithy shape ``com.amazonaws.iotwireless#SummaryMetricQueries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.summary_metric_query

SummaryMetricQueries: TypeAlias = list[
    "capo_iot_wireless.types.summary_metric_query.SummaryMetricQuery"
]


# --- restJson1 ser/de ---
def serialize_json(value: SummaryMetricQueries) -> list:
    import capo_iot_wireless.types.summary_metric_query

    out: list = []
    for item in value:
        out.append(capo_iot_wireless.types.summary_metric_query.serialize_json(item))
    return out


def deserialize_json(data: list) -> SummaryMetricQueries:
    import capo_iot_wireless.types.summary_metric_query

    out: SummaryMetricQueries = []
    for item in data:
        out.append(capo_iot_wireless.types.summary_metric_query.deserialize_json(item))
    return out
