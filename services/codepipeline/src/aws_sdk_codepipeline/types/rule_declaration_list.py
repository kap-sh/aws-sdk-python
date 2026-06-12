"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleDeclarationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.rule_declaration

RuleDeclarationList: TypeAlias = list[
    "aws_sdk_codepipeline.types.rule_declaration.RuleDeclaration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleDeclarationList) -> list:
    import aws_sdk_codepipeline.types.rule_declaration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codepipeline.types.rule_declaration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RuleDeclarationList:
    import aws_sdk_codepipeline.types.rule_declaration

    out: RuleDeclarationList = []
    for item in data:
        out.append(
            aws_sdk_codepipeline.types.rule_declaration.deserialize_aws_json_1_1(item)
        )
    return out
