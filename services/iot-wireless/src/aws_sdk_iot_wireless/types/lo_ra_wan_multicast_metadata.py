"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANMulticastMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.f_port


class LoRaWANMulticastMetadata(TypedDict, closed=True):
    f_port: NotRequired["aws_sdk_iot_wireless.types.f_port.FPort"]


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANMulticastMetadata) -> dict:
    out: dict = {}
    if "f_port" in value:
        out["FPort"] = value["f_port"]
    return out


def deserialize_json(data: dict) -> LoRaWANMulticastMetadata:
    out: LoRaWANMulticastMetadata = {}  # type: ignore[typeddict-item]
    if "FPort" in data:
        out["f_port"] = data["FPort"]
    return out
