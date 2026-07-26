"""Generated from Smithy shape ``com.amazonaws.codepipeline#StageBlockerDeclarationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.blocker_declaration

StageBlockerDeclarationList: TypeAlias = list[
    "capo_codepipeline.types.blocker_declaration.BlockerDeclaration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StageBlockerDeclarationList) -> list:
    import capo_codepipeline.types.blocker_declaration

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.blocker_declaration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> StageBlockerDeclarationList:
    import capo_codepipeline.types.blocker_declaration

    out: StageBlockerDeclarationList = []
    for item in data:
        out.append(
            capo_codepipeline.types.blocker_declaration.deserialize_aws_json_1_1(item)
        )
    return out
