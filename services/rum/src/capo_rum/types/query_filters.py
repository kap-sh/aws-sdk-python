"""Generated from Smithy shape ``com.amazonaws.rum#QueryFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rum.types.query_filter

QueryFilters: TypeAlias = list["capo_rum.types.query_filter.QueryFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: QueryFilters) -> list:
    import capo_rum.types.query_filter

    out: list = []
    for item in value:
        out.append(capo_rum.types.query_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> QueryFilters:
    import capo_rum.types.query_filter

    out: QueryFilters = []
    for item in data:
        out.append(capo_rum.types.query_filter.deserialize_json(item))
    return out
