"""Generated from Smithy shape ``com.amazonaws.iotwireless#MulticastWirelessMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.lo_ra_wan_multicast_metadata


class MulticastWirelessMetadata(TypedDict, closed=True):
    lo_ra_wan: NotRequired[
        "capo_iot_wireless.types.lo_ra_wan_multicast_metadata.LoRaWANMulticastMetadata"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: MulticastWirelessMetadata) -> dict:
    out: dict = {}
    if "lo_ra_wan" in value:
        import capo_iot_wireless.types.lo_ra_wan_multicast_metadata

        out["LoRaWAN"] = (
            capo_iot_wireless.types.lo_ra_wan_multicast_metadata.serialize_json(
                value["lo_ra_wan"]
            )
        )
    return out


def deserialize_json(data: dict) -> MulticastWirelessMetadata:
    out: MulticastWirelessMetadata = {}  # type: ignore[typeddict-item]
    if "LoRaWAN" in data:
        import capo_iot_wireless.types.lo_ra_wan_multicast_metadata

        out["lo_ra_wan"] = (
            capo_iot_wireless.types.lo_ra_wan_multicast_metadata.deserialize_json(
                data["LoRaWAN"]
            )
        )
    return out
