"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ComponentPropertyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.component_property

ComponentPropertyList: TypeAlias = list[
    "capo_amplifyuibuilder.types.component_property.ComponentProperty"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentPropertyList) -> list:
    import capo_amplifyuibuilder.types.component_property

    out: list = []
    for item in value:
        out.append(capo_amplifyuibuilder.types.component_property.serialize_json(item))
    return out


def deserialize_json(data: list) -> ComponentPropertyList:
    import capo_amplifyuibuilder.types.component_property

    out: ComponentPropertyList = []
    for item in data:
        out.append(
            capo_amplifyuibuilder.types.component_property.deserialize_json(item)
        )
    return out
