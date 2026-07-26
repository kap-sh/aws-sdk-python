"""Generated from Smithy shape ``com.amazonaws.sagemaker#MetricDataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.metric_datum

MetricDataList: TypeAlias = list["capo_sagemaker.types.metric_datum.MetricDatum"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricDataList) -> list:
    import capo_sagemaker.types.metric_datum

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.metric_datum.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MetricDataList:
    import capo_sagemaker.types.metric_datum

    out: MetricDataList = []
    for item in data:
        out.append(capo_sagemaker.types.metric_datum.deserialize_aws_json_1_1(item))
    return out
