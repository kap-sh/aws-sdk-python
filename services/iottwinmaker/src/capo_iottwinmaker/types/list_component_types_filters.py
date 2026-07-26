"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListComponentTypesFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.list_component_types_filter

ListComponentTypesFilters: TypeAlias = list[
    "capo_iottwinmaker.types.list_component_types_filter.ListComponentTypesFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListComponentTypesFilters) -> list:
    import capo_iottwinmaker.types.list_component_types_filter

    out: list = []
    for item in value:
        out.append(
            capo_iottwinmaker.types.list_component_types_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListComponentTypesFilters:
    import capo_iottwinmaker.types.list_component_types_filter

    out: ListComponentTypesFilters = []
    for item in data:
        out.append(
            capo_iottwinmaker.types.list_component_types_filter.deserialize_json(item)
        )
    return out
