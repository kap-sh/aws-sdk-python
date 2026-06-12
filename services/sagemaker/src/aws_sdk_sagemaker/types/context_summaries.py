"""Generated from Smithy shape ``com.amazonaws.sagemaker#ContextSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.context_summary

ContextSummaries: TypeAlias = list[
    "aws_sdk_sagemaker.types.context_summary.ContextSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContextSummaries) -> list:
    import aws_sdk_sagemaker.types.context_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker.types.context_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ContextSummaries:
    import aws_sdk_sagemaker.types.context_summary

    out: ContextSummaries = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.context_summary.deserialize_aws_json_1_1(item)
        )
    return out
