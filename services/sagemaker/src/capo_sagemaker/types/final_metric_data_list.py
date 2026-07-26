"""Generated from Smithy shape ``com.amazonaws.sagemaker#FinalMetricDataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.metric_data

FinalMetricDataList: TypeAlias = list["capo_sagemaker.types.metric_data.MetricData"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FinalMetricDataList) -> list:
    import capo_sagemaker.types.metric_data

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.metric_data.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FinalMetricDataList:
    import capo_sagemaker.types.metric_data

    out: FinalMetricDataList = []
    for item in data:
        out.append(capo_sagemaker.types.metric_data.deserialize_aws_json_1_1(item))
    return out
