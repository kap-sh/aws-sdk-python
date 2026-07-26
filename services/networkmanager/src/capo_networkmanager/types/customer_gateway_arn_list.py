"""Generated from Smithy shape ``com.amazonaws.networkmanager#CustomerGatewayArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.customer_gateway_arn

CustomerGatewayArnList: TypeAlias = list[
    "capo_networkmanager.types.customer_gateway_arn.CustomerGatewayArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomerGatewayArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> CustomerGatewayArnList:
    return list(data)
