"""Generated from Smithy shape ``com.amazonaws.deadline#FleetAttributeCapabilities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.fleet_attribute_capability

FleetAttributeCapabilities: TypeAlias = list[
    "aws_sdk_deadline.types.fleet_attribute_capability.FleetAttributeCapability"
]


# --- restJson1 ser/de ---
def serialize_json(value: FleetAttributeCapabilities) -> list:
    import aws_sdk_deadline.types.fleet_attribute_capability

    out: list = []
    for item in value:
        out.append(
            aws_sdk_deadline.types.fleet_attribute_capability.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FleetAttributeCapabilities:
    import aws_sdk_deadline.types.fleet_attribute_capability

    out: FleetAttributeCapabilities = []
    for item in data:
        out.append(
            aws_sdk_deadline.types.fleet_attribute_capability.deserialize_json(item)
        )
    return out
