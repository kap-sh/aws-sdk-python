"""Generated from Smithy shape ``com.amazonaws.deadline#ListAttributeCapabilityValue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.attribute_capability_value

ListAttributeCapabilityValue: TypeAlias = list[
    "capo_deadline.types.attribute_capability_value.AttributeCapabilityValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListAttributeCapabilityValue) -> list:
    return list(value)


def deserialize_json(data: list) -> ListAttributeCapabilityValue:
    return list(data)
