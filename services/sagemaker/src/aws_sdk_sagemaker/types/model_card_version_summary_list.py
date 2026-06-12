"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCardVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_card_version_summary

ModelCardVersionSummaryList: TypeAlias = list[
    "aws_sdk_sagemaker.types.model_card_version_summary.ModelCardVersionSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelCardVersionSummaryList) -> list:
    import aws_sdk_sagemaker.types.model_card_version_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.model_card_version_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ModelCardVersionSummaryList:
    import aws_sdk_sagemaker.types.model_card_version_summary

    out: ModelCardVersionSummaryList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.model_card_version_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
