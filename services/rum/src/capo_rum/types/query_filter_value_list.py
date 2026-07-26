"""Generated from Smithy shape ``com.amazonaws.rum#QueryFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rum.types.query_filter_value

QueryFilterValueList: TypeAlias = list[
    "capo_rum.types.query_filter_value.QueryFilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: QueryFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> QueryFilterValueList:
    return list(data)
