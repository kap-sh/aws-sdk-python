"""Generated from Smithy shape ``com.amazonaws.deadline#FleetAmountCapabilities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.fleet_amount_capability

FleetAmountCapabilities: TypeAlias = list[
    "aws_sdk_deadline.types.fleet_amount_capability.FleetAmountCapability"
]


# --- restJson1 ser/de ---
def serialize_json(value: FleetAmountCapabilities) -> list:
    import aws_sdk_deadline.types.fleet_amount_capability

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.fleet_amount_capability.serialize_json(item))
    return out


def deserialize_json(data: list) -> FleetAmountCapabilities:
    import aws_sdk_deadline.types.fleet_amount_capability

    out: FleetAmountCapabilities = []
    for item in data:
        out.append(
            aws_sdk_deadline.types.fleet_amount_capability.deserialize_json(item)
        )
    return out
