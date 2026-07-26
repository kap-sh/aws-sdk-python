"""Generated from Smithy shape ``com.amazonaws.frauddetector#metricDataPointsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.metric_data_point

metricDataPointsList: TypeAlias = list[
    "capo_frauddetector.types.metric_data_point.MetricDataPoint"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: metricDataPointsList) -> list:
    import capo_frauddetector.types.metric_data_point

    out: list = []
    for item in value:
        out.append(
            capo_frauddetector.types.metric_data_point.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> metricDataPointsList:
    import capo_frauddetector.types.metric_data_point

    out: metricDataPointsList = []
    for item in data:
        out.append(
            capo_frauddetector.types.metric_data_point.deserialize_aws_json_1_1(item)
        )
    return out
