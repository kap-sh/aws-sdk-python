"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#TabularPropertyValue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.property_table_value

TabularPropertyValue: TypeAlias = list[
    "capo_iottwinmaker.types.property_table_value.PropertyTableValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: TabularPropertyValue) -> list:
    import capo_iottwinmaker.types.property_table_value

    out: list = []
    for item in value:
        out.append(capo_iottwinmaker.types.property_table_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> TabularPropertyValue:
    import capo_iottwinmaker.types.property_table_value

    out: TabularPropertyValue = []
    for item in data:
        out.append(capo_iottwinmaker.types.property_table_value.deserialize_json(item))
    return out
