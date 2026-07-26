"""Generated from Smithy shape ``com.amazonaws.location#WiFiAccessPoint``."""

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError


class WiFiAccessPoint(TypedDict, closed=True):
    mac_address: "str"
    """<p>Medium access control address (Mac).</p>"""
    rss: "int"
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
