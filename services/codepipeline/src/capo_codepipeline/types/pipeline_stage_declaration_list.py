"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineStageDeclarationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.stage_declaration

PipelineStageDeclarationList: TypeAlias = list[
    "capo_codepipeline.types.stage_declaration.StageDeclaration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineStageDeclarationList) -> list:
    import capo_codepipeline.types.stage_declaration

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.stage_declaration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PipelineStageDeclarationList:
    import capo_codepipeline.types.stage_declaration

    out: PipelineStageDeclarationList = []
    for item in data:
        out.append(
            capo_codepipeline.types.stage_declaration.deserialize_aws_json_1_1(item)
        )
    return out
