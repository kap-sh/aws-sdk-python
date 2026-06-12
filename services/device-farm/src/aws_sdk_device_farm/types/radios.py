"""Generated from Smithy shape ``com.amazonaws.devicefarm#Radios``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.boolean


class Radios(TypedDict):
    wifi: NotRequired["aws_sdk_device_farm.types.boolean.Boolean"]
    """<p>True if Wi-Fi is enabled at the beginning of the test. Otherwise, false.</p>"""
    bluetooth: NotRequired["aws_sdk_device_farm.types.boolean.Boolean"]
    """<p>True if Bluetooth is enabled at the beginning of the test. Otherwise, false.</p>"""
    nfc: NotRequired["aws_sdk_device_farm.types.boolean.Boolean"]
    """<p>True if NFC is enabled at the beginning of the test. Otherwise, false.</p>"""
    gps: NotRequired["aws_sdk_device_farm.types.boolean.Boolean"]
    """<p>True if GPS is enabled at the beginning of the test. Otherwise, false.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Radios) -> dict:
    out: dict = {}
    if "wifi" in value:
        out["wifi"] = value["wifi"]
    if "bluetooth" in value:
        out["bluetooth"] = value["bluetooth"]
    if "nfc" in value:
        out["nfc"] = value["nfc"]
    if "gps" in value:
        out["gps"] = value["gps"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Radios:
    out: Radios = {}  # type: ignore[typeddict-item]
    if "wifi" in data:
        out["wifi"] = data["wifi"]
    if "bluetooth" in data:
        out["bluetooth"] = data["bluetooth"]
    if "nfc" in data:
        out["nfc"] = data["nfc"]
    if "gps" in data:
        out["gps"] = data["gps"]
    return out
