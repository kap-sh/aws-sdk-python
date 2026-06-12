"""Generated from Smithy shape ``com.amazonaws.deadline#SearchFilterExpressions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.search_filter_expression

SearchFilterExpressions: TypeAlias = list[
    "aws_sdk_deadline.types.search_filter_expression.SearchFilterExpression"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchFilterExpressions) -> list:
    import aws_sdk_deadline.types.search_filter_expression

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.search_filter_expression.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchFilterExpressions:
    import aws_sdk_deadline.types.search_filter_expression

    out: SearchFilterExpressions = []
    for item in data:
        out.append(
            aws_sdk_deadline.types.search_filter_expression.deserialize_json(item)
        )
    return out
