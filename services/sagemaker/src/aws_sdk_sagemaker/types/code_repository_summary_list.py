"""Generated from Smithy shape ``com.amazonaws.sagemaker#CodeRepositorySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.code_repository_summary

CodeRepositorySummaryList: TypeAlias = list[
    "aws_sdk_sagemaker.types.code_repository_summary.CodeRepositorySummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeRepositorySummaryList) -> list:
    import aws_sdk_sagemaker.types.code_repository_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.code_repository_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CodeRepositorySummaryList:
    import aws_sdk_sagemaker.types.code_repository_summary

    out: CodeRepositorySummaryList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.code_repository_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
