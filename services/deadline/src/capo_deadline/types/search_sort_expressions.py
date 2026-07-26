"""Generated from Smithy shape ``com.amazonaws.deadline#SearchSortExpressions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.search_sort_expression

SearchSortExpressions: TypeAlias = list[
    "capo_deadline.types.search_sort_expression.SearchSortExpression"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchSortExpressions) -> list:
    import capo_deadline.types.search_sort_expression

    out: list = []
    for item in value:
        out.append(capo_deadline.types.search_sort_expression.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchSortExpressions:
    import capo_deadline.types.search_sort_expression

    out: SearchSortExpressions = []
    for item in data:
        out.append(capo_deadline.types.search_sort_expression.deserialize_json(item))
    return out
