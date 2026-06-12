"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANGatewayMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.lo_ra_wan_gateway_metadata

LoRaWANGatewayMetadataList: TypeAlias = list[
    "aws_sdk_iot_wireless.types.lo_ra_wan_gateway_metadata.LoRaWANGatewayMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANGatewayMetadataList) -> list:
    import aws_sdk_iot_wireless.types.lo_ra_wan_gateway_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_wireless.types.lo_ra_wan_gateway_metadata.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> LoRaWANGatewayMetadataList:
    import aws_sdk_iot_wireless.types.lo_ra_wan_gateway_metadata

    out: LoRaWANGatewayMetadataList = []
    for item in data:
        out.append(
            aws_sdk_iot_wireless.types.lo_ra_wan_gateway_metadata.deserialize_json(item)
        )
    return out
