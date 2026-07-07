"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANListDevice``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.dev_eui


class LoRaWANListDevice(TypedDict, closed=True):
    dev_eui: NotRequired["aws_sdk_iot_wireless.types.dev_eui.DevEui"]
    """<p>The DevEUI value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANListDevice) -> dict:
    out: dict = {}
    if "dev_eui" in value:
        out["DevEui"] = value["dev_eui"]
    return out


def deserialize_json(data: dict) -> LoRaWANListDevice:
    out: LoRaWANListDevice = {}  # type: ignore[typeddict-item]
    if "DevEui" in data:
        out["dev_eui"] = data["DevEui"]
    return out
