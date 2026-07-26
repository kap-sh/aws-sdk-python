"""Generated from Smithy shape ``com.amazonaws.frauddetector#ATIMetricDataPointsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.ati_metric_data_point

ATIMetricDataPointsList: TypeAlias = list[
    "capo_frauddetector.types.ati_metric_data_point.ATIMetricDataPoint"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ATIMetricDataPointsList) -> list:
    import capo_frauddetector.types.ati_metric_data_point

    out: list = []
    for item in value:
        out.append(
            capo_frauddetector.types.ati_metric_data_point.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ATIMetricDataPointsList:
    import capo_frauddetector.types.ati_metric_data_point

    out: ATIMetricDataPointsList = []
    for item in data:
        out.append(
            capo_frauddetector.types.ati_metric_data_point.deserialize_aws_json_1_1(
                item
            )
        )
    return out
