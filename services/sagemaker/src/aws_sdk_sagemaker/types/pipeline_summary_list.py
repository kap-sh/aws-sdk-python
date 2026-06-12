"""Generated from Smithy shape ``com.amazonaws.sagemaker#PipelineSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.pipeline_summary

PipelineSummaryList: TypeAlias = list[
    "aws_sdk_sagemaker.types.pipeline_summary.PipelineSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineSummaryList) -> list:
    import aws_sdk_sagemaker.types.pipeline_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.pipeline_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PipelineSummaryList:
    import aws_sdk_sagemaker.types.pipeline_summary

    out: PipelineSummaryList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.pipeline_summary.deserialize_aws_json_1_1(item)
        )
    return out
