"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProjectSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.project_summary

ProjectSummaryList: TypeAlias = list[
    "aws_sdk_sagemaker.types.project_summary.ProjectSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectSummaryList) -> list:
    import aws_sdk_sagemaker.types.project_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker.types.project_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ProjectSummaryList:
    import aws_sdk_sagemaker.types.project_summary

    out: ProjectSummaryList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.project_summary.deserialize_aws_json_1_1(item)
        )
    return out
