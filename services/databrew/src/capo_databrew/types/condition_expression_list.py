"""Generated from Smithy shape ``com.amazonaws.databrew#ConditionExpressionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_databrew.types.condition_expression

ConditionExpressionList: TypeAlias = list[
    "capo_databrew.types.condition_expression.ConditionExpression"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConditionExpressionList) -> list:
    import capo_databrew.types.condition_expression

    out: list = []
    for item in value:
        out.append(capo_databrew.types.condition_expression.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConditionExpressionList:
    import capo_databrew.types.condition_expression

    out: ConditionExpressionList = []
    for item in data:
        out.append(capo_databrew.types.condition_expression.deserialize_json(item))
    return out
