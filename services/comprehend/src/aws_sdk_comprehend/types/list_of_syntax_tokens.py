"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfSyntaxTokens``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.syntax_token

ListOfSyntaxTokens: TypeAlias = list[
    "aws_sdk_comprehend.types.syntax_token.SyntaxToken"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfSyntaxTokens) -> list:
    import aws_sdk_comprehend.types.syntax_token

    out: list = []
    for item in value:
        out.append(aws_sdk_comprehend.types.syntax_token.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfSyntaxTokens:
    import aws_sdk_comprehend.types.syntax_token

    out: ListOfSyntaxTokens = []
    for item in data:
        out.append(aws_sdk_comprehend.types.syntax_token.deserialize_aws_json_1_1(item))
    return out
