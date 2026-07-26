"""Generated from Smithy shape ``com.amazonaws.glue#FilterExpressions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.filter_expression

FilterExpressions: TypeAlias = list[
    "capo_glue.types.filter_expression.FilterExpression"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterExpressions) -> list:
    import capo_glue.types.filter_expression

    out: list = []
    for item in value:
        out.append(capo_glue.types.filter_expression.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FilterExpressions:
    import capo_glue.types.filter_expression

    out: FilterExpressions = []
    for item in data:
        out.append(capo_glue.types.filter_expression.deserialize_aws_json_1_1(item))
    return out
