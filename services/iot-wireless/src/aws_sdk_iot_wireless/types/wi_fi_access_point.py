"""Generated from Smithy shape ``com.amazonaws.iotwireless#WiFiAccessPoint``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.mac_address
    import aws_sdk_iot_wireless.types.rss


class WiFiAccessPoint(TypedDict):
    mac_address: "aws_sdk_iot_wireless.types.mac_address.MacAddress"
    """<p>Wi-Fi MAC Address.</p>"""
    rss: "aws_sdk_iot_wireless.types.rss.RSS"
    """<p>Received signal strength (dBm) of the WLAN measurement data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WiFiAccessPoint) -> dict:
    out: dict = {}
    out["MacAddress"] = value["mac_address"]
    out["Rss"] = value["rss"]
    return out


def deserialize_json(data: dict) -> WiFiAccessPoint:
    out: WiFiAccessPoint = {}  # type: ignore[typeddict-item]
    if "MacAddress" in data:
        out["mac_address"] = data["MacAddress"]
    else:
        raise DeserializationError("WiFiAccessPoint.mac_address required")
    if "Rss" in data:
        out["rss"] = data["Rss"]
    else:
        raise DeserializationError("WiFiAccessPoint.rss required")
    return out
