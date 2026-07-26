"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#TabularPropertyValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.tabular_property_value

TabularPropertyValues: TypeAlias = list[
    "capo_iottwinmaker.types.tabular_property_value.TabularPropertyValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: TabularPropertyValues) -> list:
    import capo_iottwinmaker.types.tabular_property_value

    out: list = []
    for item in value:
        out.append(capo_iottwinmaker.types.tabular_property_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> TabularPropertyValues:
    import capo_iottwinmaker.types.tabular_property_value

    out: TabularPropertyValues = []
    for item in data:
        out.append(
            capo_iottwinmaker.types.tabular_property_value.deserialize_json(item)
        )
    return out
