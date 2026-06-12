"""Generated from Smithy shape ``com.amazonaws.glue#ConditionExpressionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.condition_expression

ConditionExpressionList: TypeAlias = list[
    "aws_sdk_glue.types.condition_expression.ConditionExpression"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConditionExpressionList) -> list:
    import aws_sdk_glue.types.condition_expression

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.condition_expression.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ConditionExpressionList:
    import aws_sdk_glue.types.condition_expression

    out: ConditionExpressionList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.condition_expression.deserialize_aws_json_1_1(item)
        )
    return out
