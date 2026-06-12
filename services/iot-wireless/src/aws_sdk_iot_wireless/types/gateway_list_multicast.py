"""Generated from Smithy shape ``com.amazonaws.iotwireless#GatewayListMulticast``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.wireless_gateway_id

GatewayListMulticast: TypeAlias = list[
    "aws_sdk_iot_wireless.types.wireless_gateway_id.WirelessGatewayId"
]


# --- restJson1 ser/de ---
def serialize_json(value: GatewayListMulticast) -> list:
    return list(value)


def deserialize_json(data: list) -> GatewayListMulticast:
    return list(data)
