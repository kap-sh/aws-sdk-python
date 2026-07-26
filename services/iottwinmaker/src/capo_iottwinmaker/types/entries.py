"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#Entries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.property_value_entry

Entries: TypeAlias = list[
    "capo_iottwinmaker.types.property_value_entry.PropertyValueEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: Entries) -> list:
    import capo_iottwinmaker.types.property_value_entry

    out: list = []
    for item in value:
        out.append(capo_iottwinmaker.types.property_value_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> Entries:
    import capo_iottwinmaker.types.property_value_entry

    out: Entries = []
    for item in data:
        out.append(capo_iottwinmaker.types.property_value_entry.deserialize_json(item))
    return out
