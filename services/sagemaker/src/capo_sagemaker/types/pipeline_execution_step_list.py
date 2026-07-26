"""Generated from Smithy shape ``com.amazonaws.sagemaker#PipelineExecutionStepList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.pipeline_execution_step

PipelineExecutionStepList: TypeAlias = list[
    "capo_sagemaker.types.pipeline_execution_step.PipelineExecutionStep"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineExecutionStepList) -> list:
    import capo_sagemaker.types.pipeline_execution_step

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.pipeline_execution_step.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PipelineExecutionStepList:
    import capo_sagemaker.types.pipeline_execution_step

    out: PipelineExecutionStepList = []
    for item in data:
        out.append(
            capo_sagemaker.types.pipeline_execution_step.deserialize_aws_json_1_1(item)
        )
    return out
