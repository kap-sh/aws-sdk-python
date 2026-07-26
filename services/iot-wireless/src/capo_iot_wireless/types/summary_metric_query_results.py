"""Generated from Smithy shape ``com.amazonaws.iotwireless#SummaryMetricQueryResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.summary_metric_query_result

SummaryMetricQueryResults: TypeAlias = list[
    "capo_iot_wireless.types.summary_metric_query_result.SummaryMetricQueryResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: SummaryMetricQueryResults) -> list:
    import capo_iot_wireless.types.summary_metric_query_result

    out: list = []
    for item in value:
        out.append(
            capo_iot_wireless.types.summary_metric_query_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SummaryMetricQueryResults:
    import capo_iot_wireless.types.summary_metric_query_result

    out: SummaryMetricQueryResults = []
    for item in data:
        out.append(
            capo_iot_wireless.types.summary_metric_query_result.deserialize_json(item)
        )
    return out
