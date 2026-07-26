"""Generated from Smithy shape ``com.amazonaws.connect#PrimaryAttributeValuesSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.primary_attribute_value

PrimaryAttributeValuesSet: TypeAlias = list[
    "capo_connect.types.primary_attribute_value.PrimaryAttributeValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrimaryAttributeValuesSet) -> list:
    import capo_connect.types.primary_attribute_value

    out: list = []
    for item in value:
        out.append(capo_connect.types.primary_attribute_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> PrimaryAttributeValuesSet:
    import capo_connect.types.primary_attribute_value

    out: PrimaryAttributeValuesSet = []
    for item in data:
        out.append(capo_connect.types.primary_attribute_value.deserialize_json(item))
    return out
