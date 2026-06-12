"""Generated from Smithy shape ``com.amazonaws.iotwireless#SummaryMetricQueryResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.summary_metric_query_result

SummaryMetricQueryResults: TypeAlias = list[
    "aws_sdk_iot_wireless.types.summary_metric_query_result.SummaryMetricQueryResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: SummaryMetricQueryResults) -> list:
    import aws_sdk_iot_wireless.types.summary_metric_query_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_wireless.types.summary_metric_query_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SummaryMetricQueryResults:
    import aws_sdk_iot_wireless.types.summary_metric_query_result

    out: SummaryMetricQueryResults = []
    for item in data:
        out.append(
            aws_sdk_iot_wireless.types.summary_metric_query_result.deserialize_json(
                item
            )
        )
    return out
