"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCardSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_card_summary

ModelCardSummaryList: TypeAlias = list[
    "aws_sdk_sagemaker.types.model_card_summary.ModelCardSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelCardSummaryList) -> list:
    import aws_sdk_sagemaker.types.model_card_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.model_card_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ModelCardSummaryList:
    import aws_sdk_sagemaker.types.model_card_summary

    out: ModelCardSummaryList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.model_card_summary.deserialize_aws_json_1_1(item)
        )
    return out
