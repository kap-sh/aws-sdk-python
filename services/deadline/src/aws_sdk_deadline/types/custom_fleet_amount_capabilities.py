"""Generated from Smithy shape ``com.amazonaws.deadline#CustomFleetAmountCapabilities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.fleet_amount_capability

CustomFleetAmountCapabilities: TypeAlias = list[
    "aws_sdk_deadline.types.fleet_amount_capability.FleetAmountCapability"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomFleetAmountCapabilities) -> list:
    import aws_sdk_deadline.types.fleet_amount_capability

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.fleet_amount_capability.serialize_json(item))
    return out


def deserialize_json(data: list) -> CustomFleetAmountCapabilities:
    import aws_sdk_deadline.types.fleet_amount_capability

    out: CustomFleetAmountCapabilities = []
    for item in data:
        out.append(
            aws_sdk_deadline.types.fleet_amount_capability.deserialize_json(item)
        )
    return out
