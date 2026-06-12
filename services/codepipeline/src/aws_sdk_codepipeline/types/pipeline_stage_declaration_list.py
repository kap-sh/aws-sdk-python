"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineStageDeclarationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.stage_declaration

PipelineStageDeclarationList: TypeAlias = list[
    "aws_sdk_codepipeline.types.stage_declaration.StageDeclaration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineStageDeclarationList) -> list:
    import aws_sdk_codepipeline.types.stage_declaration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codepipeline.types.stage_declaration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PipelineStageDeclarationList:
    import aws_sdk_codepipeline.types.stage_declaration

    out: PipelineStageDeclarationList = []
    for item in data:
        out.append(
            aws_sdk_codepipeline.types.stage_declaration.deserialize_aws_json_1_1(item)
        )
    return out
