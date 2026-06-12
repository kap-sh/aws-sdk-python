"""Generated from Smithy shape ``com.amazonaws.lakeformation#LFTagExpressionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.lf_tag_expression

LFTagExpressionsList: TypeAlias = list[
    "aws_sdk_lakeformation.types.lf_tag_expression.LFTagExpression"
]


# --- restJson1 ser/de ---
def serialize_json(value: LFTagExpressionsList) -> list:
    import aws_sdk_lakeformation.types.lf_tag_expression

    out: list = []
    for item in value:
        out.append(aws_sdk_lakeformation.types.lf_tag_expression.serialize_json(item))
    return out


def deserialize_json(data: list) -> LFTagExpressionsList:
    import aws_sdk_lakeformation.types.lf_tag_expression

    out: LFTagExpressionsList = []
    for item in data:
        out.append(aws_sdk_lakeformation.types.lf_tag_expression.deserialize_json(item))
    return out
