"""Generated from Smithy shape ``com.amazonaws.glue#FilterExpressions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.filter_expression

FilterExpressions: TypeAlias = list[
    "aws_sdk_glue.types.filter_expression.FilterExpression"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterExpressions) -> list:
    import aws_sdk_glue.types.filter_expression

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.filter_expression.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FilterExpressions:
    import aws_sdk_glue.types.filter_expression

    out: FilterExpressions = []
    for item in data:
        out.append(aws_sdk_glue.types.filter_expression.deserialize_aws_json_1_1(item))
    return out
