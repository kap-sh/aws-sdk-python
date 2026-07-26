"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListEntitiesFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.list_entities_filter

ListEntitiesFilters: TypeAlias = list[
    "capo_iottwinmaker.types.list_entities_filter.ListEntitiesFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListEntitiesFilters) -> list:
    import capo_iottwinmaker.types.list_entities_filter

    out: list = []
    for item in value:
        out.append(capo_iottwinmaker.types.list_entities_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListEntitiesFilters:
    import capo_iottwinmaker.types.list_entities_filter

    out: ListEntitiesFilters = []
    for item in data:
        out.append(capo_iottwinmaker.types.list_entities_filter.deserialize_json(item))
    return out
