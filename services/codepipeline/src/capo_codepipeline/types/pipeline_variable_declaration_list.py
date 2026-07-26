"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineVariableDeclarationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.pipeline_variable_declaration

PipelineVariableDeclarationList: TypeAlias = list[
    "capo_codepipeline.types.pipeline_variable_declaration.PipelineVariableDeclaration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineVariableDeclarationList) -> list:
    import capo_codepipeline.types.pipeline_variable_declaration

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.pipeline_variable_declaration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PipelineVariableDeclarationList:
    import capo_codepipeline.types.pipeline_variable_declaration

    out: PipelineVariableDeclarationList = []
    for item in data:
        out.append(
            capo_codepipeline.types.pipeline_variable_declaration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
