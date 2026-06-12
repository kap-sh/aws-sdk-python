"""Generated from Smithy shape ``com.amazonaws.sagemaker#PipelineVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.pipeline_version_summary

PipelineVersionSummaryList: TypeAlias = list[
    "aws_sdk_sagemaker.types.pipeline_version_summary.PipelineVersionSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineVersionSummaryList) -> list:
    import aws_sdk_sagemaker.types.pipeline_version_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.pipeline_version_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PipelineVersionSummaryList:
    import aws_sdk_sagemaker.types.pipeline_version_summary

    out: PipelineVersionSummaryList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.pipeline_version_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
