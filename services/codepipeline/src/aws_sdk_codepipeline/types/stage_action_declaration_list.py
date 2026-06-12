"""Generated from Smithy shape ``com.amazonaws.codepipeline#StageActionDeclarationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.action_declaration

StageActionDeclarationList: TypeAlias = list[
    "aws_sdk_codepipeline.types.action_declaration.ActionDeclaration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StageActionDeclarationList) -> list:
    import aws_sdk_codepipeline.types.action_declaration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codepipeline.types.action_declaration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> StageActionDeclarationList:
    import aws_sdk_codepipeline.types.action_declaration

    out: StageActionDeclarationList = []
    for item in data:
        out.append(
            aws_sdk_codepipeline.types.action_declaration.deserialize_aws_json_1_1(item)
        )
    return out
