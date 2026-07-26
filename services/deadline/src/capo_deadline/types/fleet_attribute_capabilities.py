"""Generated from Smithy shape ``com.amazonaws.deadline#FleetAttributeCapabilities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.fleet_attribute_capability

FleetAttributeCapabilities: TypeAlias = list[
    "capo_deadline.types.fleet_attribute_capability.FleetAttributeCapability"
]


# --- restJson1 ser/de ---
def serialize_json(value: FleetAttributeCapabilities) -> list:
    import capo_deadline.types.fleet_attribute_capability

    out: list = []
    for item in value:
        out.append(capo_deadline.types.fleet_attribute_capability.serialize_json(item))
    return out


def deserialize_json(data: list) -> FleetAttributeCapabilities:
    import capo_deadline.types.fleet_attribute_capability

    out: FleetAttributeCapabilities = []
    for item in data:
        out.append(
            capo_deadline.types.fleet_attribute_capability.deserialize_json(item)
        )
    return out
