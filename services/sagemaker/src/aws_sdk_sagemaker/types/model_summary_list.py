"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_summary

ModelSummaryList: TypeAlias = list["aws_sdk_sagemaker.types.model_summary.ModelSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelSummaryList) -> list:
    import aws_sdk_sagemaker.types.model_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker.types.model_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ModelSummaryList:
    import aws_sdk_sagemaker.types.model_summary

    out: ModelSummaryList = []
    for item in data:
        out.append(aws_sdk_sagemaker.types.model_summary.deserialize_aws_json_1_1(item))
    return out
