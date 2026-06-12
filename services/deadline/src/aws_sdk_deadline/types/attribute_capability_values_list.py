"""Generated from Smithy shape ``com.amazonaws.deadline#AttributeCapabilityValuesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.attribute_capability_value

AttributeCapabilityValuesList: TypeAlias = list[
    "aws_sdk_deadline.types.attribute_capability_value.AttributeCapabilityValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeCapabilityValuesList) -> list:
    return list(value)


def deserialize_json(data: list) -> AttributeCapabilityValuesList:
    return list(data)
