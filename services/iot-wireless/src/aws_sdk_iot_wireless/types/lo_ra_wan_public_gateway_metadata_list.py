"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANPublicGatewayMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.lo_ra_wan_public_gateway_metadata

LoRaWANPublicGatewayMetadataList: TypeAlias = list[
    "aws_sdk_iot_wireless.types.lo_ra_wan_public_gateway_metadata.LoRaWANPublicGatewayMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANPublicGatewayMetadataList) -> list:
    import aws_sdk_iot_wireless.types.lo_ra_wan_public_gateway_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_wireless.types.lo_ra_wan_public_gateway_metadata.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> LoRaWANPublicGatewayMetadataList:
    import aws_sdk_iot_wireless.types.lo_ra_wan_public_gateway_metadata

    out: LoRaWANPublicGatewayMetadataList = []
    for item in data:
        out.append(
            aws_sdk_iot_wireless.types.lo_ra_wan_public_gateway_metadata.deserialize_json(
                item
            )
        )
    return out
