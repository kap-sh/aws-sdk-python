"""Generated from Smithy shape ``com.amazonaws.deadline#CustomFleetAttributeCapabilities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.fleet_attribute_capability

CustomFleetAttributeCapabilities: TypeAlias = list[
    "capo_deadline.types.fleet_attribute_capability.FleetAttributeCapability"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomFleetAttributeCapabilities) -> list:
    import capo_deadline.types.fleet_attribute_capability

    out: list = []
    for item in value:
        out.append(capo_deadline.types.fleet_attribute_capability.serialize_json(item))
    return out


def deserialize_json(data: list) -> CustomFleetAttributeCapabilities:
    import capo_deadline.types.fleet_attribute_capability

    out: CustomFleetAttributeCapabilities = []
    for item in data:
        out.append(
            capo_deadline.types.fleet_attribute_capability.deserialize_json(item)
        )
    return out
