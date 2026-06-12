"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.inference_component_summary

InferenceComponentSummaryList: TypeAlias = list[
    "aws_sdk_sagemaker.types.inference_component_summary.InferenceComponentSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceComponentSummaryList) -> list:
    import aws_sdk_sagemaker.types.inference_component_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.inference_component_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InferenceComponentSummaryList:
    import aws_sdk_sagemaker.types.inference_component_summary

    out: InferenceComponentSummaryList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.inference_component_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
