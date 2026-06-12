"""Generated from Smithy shape ``com.amazonaws.sagemaker#MetricDataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.metric_datum

MetricDataList: TypeAlias = list["aws_sdk_sagemaker.types.metric_datum.MetricDatum"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricDataList) -> list:
    import aws_sdk_sagemaker.types.metric_datum

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker.types.metric_datum.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MetricDataList:
    import aws_sdk_sagemaker.types.metric_datum

    out: MetricDataList = []
    for item in data:
        out.append(aws_sdk_sagemaker.types.metric_datum.deserialize_aws_json_1_1(item))
    return out
