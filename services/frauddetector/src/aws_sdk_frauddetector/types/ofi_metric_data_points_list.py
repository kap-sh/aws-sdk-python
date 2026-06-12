"""Generated from Smithy shape ``com.amazonaws.frauddetector#OFIMetricDataPointsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.ofi_metric_data_point

OFIMetricDataPointsList: TypeAlias = list[
    "aws_sdk_frauddetector.types.ofi_metric_data_point.OFIMetricDataPoint"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OFIMetricDataPointsList) -> list:
    import aws_sdk_frauddetector.types.ofi_metric_data_point

    out: list = []
    for item in value:
        out.append(
            aws_sdk_frauddetector.types.ofi_metric_data_point.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OFIMetricDataPointsList:
    import aws_sdk_frauddetector.types.ofi_metric_data_point

    out: OFIMetricDataPointsList = []
    for item in data:
        out.append(
            aws_sdk_frauddetector.types.ofi_metric_data_point.deserialize_aws_json_1_1(
                item
            )
        )
    return out
