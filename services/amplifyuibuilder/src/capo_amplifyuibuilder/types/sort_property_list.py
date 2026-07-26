"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#SortPropertyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.sort_property

SortPropertyList: TypeAlias = list[
    "capo_amplifyuibuilder.types.sort_property.SortProperty"
]


# --- restJson1 ser/de ---
def serialize_json(value: SortPropertyList) -> list:
    import capo_amplifyuibuilder.types.sort_property

    out: list = []
    for item in value:
        out.append(capo_amplifyuibuilder.types.sort_property.serialize_json(item))
    return out


def deserialize_json(data: list) -> SortPropertyList:
    import capo_amplifyuibuilder.types.sort_property

    out: SortPropertyList = []
    for item in data:
        out.append(capo_amplifyuibuilder.types.sort_property.deserialize_json(item))
    return out
