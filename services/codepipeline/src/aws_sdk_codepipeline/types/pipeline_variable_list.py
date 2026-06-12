"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineVariableList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.pipeline_variable

PipelineVariableList: TypeAlias = list[
    "aws_sdk_codepipeline.types.pipeline_variable.PipelineVariable"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineVariableList) -> list:
    import aws_sdk_codepipeline.types.pipeline_variable

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codepipeline.types.pipeline_variable.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PipelineVariableList:
    import aws_sdk_codepipeline.types.pipeline_variable

    out: PipelineVariableList = []
    for item in data:
        out.append(
            aws_sdk_codepipeline.types.pipeline_variable.deserialize_aws_json_1_1(item)
        )
    return out
