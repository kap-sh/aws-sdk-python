"""Generated from Smithy shape ``com.amazonaws.codepipeline#ResolvedPipelineVariableList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.resolved_pipeline_variable

ResolvedPipelineVariableList: TypeAlias = list[
    "capo_codepipeline.types.resolved_pipeline_variable.ResolvedPipelineVariable"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolvedPipelineVariableList) -> list:
    import capo_codepipeline.types.resolved_pipeline_variable

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.resolved_pipeline_variable.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResolvedPipelineVariableList:
    import capo_codepipeline.types.resolved_pipeline_variable

    out: ResolvedPipelineVariableList = []
    for item in data:
        out.append(
            capo_codepipeline.types.resolved_pipeline_variable.deserialize_aws_json_1_1(
                item
            )
        )
    return out
