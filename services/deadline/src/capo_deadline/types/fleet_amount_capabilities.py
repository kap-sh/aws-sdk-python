"""Generated from Smithy shape ``com.amazonaws.deadline#FleetAmountCapabilities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.fleet_amount_capability

FleetAmountCapabilities: TypeAlias = list[
    "capo_deadline.types.fleet_amount_capability.FleetAmountCapability"
]


# --- restJson1 ser/de ---
def serialize_json(value: FleetAmountCapabilities) -> list:
    import capo_deadline.types.fleet_amount_capability

    out: list = []
    for item in value:
        out.append(capo_deadline.types.fleet_amount_capability.serialize_json(item))
    return out


def deserialize_json(data: list) -> FleetAmountCapabilities:
    import capo_deadline.types.fleet_amount_capability

    out: FleetAmountCapabilities = []
    for item in data:
        out.append(capo_deadline.types.fleet_amount_capability.deserialize_json(item))
    return out
