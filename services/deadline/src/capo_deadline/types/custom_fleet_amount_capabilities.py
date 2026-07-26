"""Generated from Smithy shape ``com.amazonaws.deadline#CustomFleetAmountCapabilities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.fleet_amount_capability

CustomFleetAmountCapabilities: TypeAlias = list[
    "capo_deadline.types.fleet_amount_capability.FleetAmountCapability"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomFleetAmountCapabilities) -> list:
    import capo_deadline.types.fleet_amount_capability

    out: list = []
    for item in value:
        out.append(capo_deadline.types.fleet_amount_capability.serialize_json(item))
    return out


def deserialize_json(data: list) -> CustomFleetAmountCapabilities:
    import capo_deadline.types.fleet_amount_capability

    out: CustomFleetAmountCapabilities = []
    for item in data:
        out.append(capo_deadline.types.fleet_amount_capability.deserialize_json(item))
    return out
