"""Generated from Smithy shape ``com.amazonaws.codepipeline#StageBlockerDeclarationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.blocker_declaration

StageBlockerDeclarationList: TypeAlias = list[
    "aws_sdk_codepipeline.types.blocker_declaration.BlockerDeclaration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StageBlockerDeclarationList) -> list:
    import aws_sdk_codepipeline.types.blocker_declaration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codepipeline.types.blocker_declaration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> StageBlockerDeclarationList:
    import aws_sdk_codepipeline.types.blocker_declaration

    out: StageBlockerDeclarationList = []
    for item in data:
        out.append(
            aws_sdk_codepipeline.types.blocker_declaration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
