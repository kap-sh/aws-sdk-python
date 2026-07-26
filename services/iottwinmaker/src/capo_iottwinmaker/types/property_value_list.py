"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.property_value_history

PropertyValueList: TypeAlias = list[
    "capo_iottwinmaker.types.property_value_history.PropertyValueHistory"
]


# --- restJson1 ser/de ---
def serialize_json(value: PropertyValueList) -> list:
    import capo_iottwinmaker.types.property_value_history

    out: list = []
    for item in value:
        out.append(capo_iottwinmaker.types.property_value_history.serialize_json(item))
    return out


def deserialize_json(data: list) -> PropertyValueList:
    import capo_iottwinmaker.types.property_value_history

    out: PropertyValueList = []
    for item in data:
        out.append(
            capo_iottwinmaker.types.property_value_history.deserialize_json(item)
        )
    return out
