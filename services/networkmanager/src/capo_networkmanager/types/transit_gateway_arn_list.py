"""Generated from Smithy shape ``com.amazonaws.networkmanager#TransitGatewayArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.transit_gateway_arn

TransitGatewayArnList: TypeAlias = list[
    "capo_networkmanager.types.transit_gateway_arn.TransitGatewayArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: TransitGatewayArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> TransitGatewayArnList:
    return list(data)
