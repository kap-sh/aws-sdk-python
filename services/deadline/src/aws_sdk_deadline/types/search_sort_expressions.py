"""Generated from Smithy shape ``com.amazonaws.deadline#SearchSortExpressions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.search_sort_expression

SearchSortExpressions: TypeAlias = list[
    "aws_sdk_deadline.types.search_sort_expression.SearchSortExpression"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchSortExpressions) -> list:
    import aws_sdk_deadline.types.search_sort_expression

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.search_sort_expression.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchSortExpressions:
    import aws_sdk_deadline.types.search_sort_expression

    out: SearchSortExpressions = []
    for item in data:
        out.append(aws_sdk_deadline.types.search_sort_expression.deserialize_json(item))
    return out
