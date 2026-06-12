"""Generated from Smithy shape ``com.amazonaws.iotwireless#MulticastWirelessMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.lo_ra_wan_multicast_metadata


class MulticastWirelessMetadata(TypedDict):
    lo_ra_wan: NotRequired[
        "aws_sdk_iot_wireless.types.lo_ra_wan_multicast_metadata.LoRaWANMulticastMetadata"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: MulticastWirelessMetadata) -> dict:
    out: dict = {}
    if "lo_ra_wan" in value:
        import aws_sdk_iot_wireless.types.lo_ra_wan_multicast_metadata

        out["LoRaWAN"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_multicast_metadata.serialize_json(
                value["lo_ra_wan"]
            )
        )
    return out


def deserialize_json(data: dict) -> MulticastWirelessMetadata:
    out: MulticastWirelessMetadata = {}  # type: ignore[typeddict-item]
    if "LoRaWAN" in data:
        import aws_sdk_iot_wireless.types.lo_ra_wan_multicast_metadata

        out["lo_ra_wan"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_multicast_metadata.deserialize_json(
                data["LoRaWAN"]
            )
        )
    return out
