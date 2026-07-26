"""Generated from Smithy shape ``com.amazonaws.sagemaker#PipelineExecutionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.pipeline_execution_summary

PipelineExecutionSummaryList: TypeAlias = list[
    "capo_sagemaker.types.pipeline_execution_summary.PipelineExecutionSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineExecutionSummaryList) -> list:
    import capo_sagemaker.types.pipeline_execution_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.pipeline_execution_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PipelineExecutionSummaryList:
    import capo_sagemaker.types.pipeline_execution_summary

    out: PipelineExecutionSummaryList = []
    for item in data:
        out.append(
            capo_sagemaker.types.pipeline_execution_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
