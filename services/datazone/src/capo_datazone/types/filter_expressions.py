"""Generated from Smithy shape ``com.amazonaws.datazone#FilterExpressions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.filter_expression

FilterExpressions: TypeAlias = list[
    "capo_datazone.types.filter_expression.FilterExpression"
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterExpressions) -> list:
    import capo_datazone.types.filter_expression

    out: list = []
    for item in value:
        out.append(capo_datazone.types.filter_expression.serialize_json(item))
    return out


def deserialize_json(data: list) -> FilterExpressions:
    import capo_datazone.types.filter_expression

    out: FilterExpressions = []
    for item in data:
        out.append(capo_datazone.types.filter_expression.deserialize_json(item))
    return out
