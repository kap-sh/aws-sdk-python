"""Generated from Smithy shape ``com.amazonaws.iotwireless#Ip``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.ip_address


class Ip(TypedDict):
    ip_address: "aws_sdk_iot_wireless.types.ip_address.IPAddress"
    """<p>IP address information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ip) -> dict:
    out: dict = {}
    out["IpAddress"] = value["ip_address"]
    return out


def deserialize_json(data: dict) -> Ip:
    out: Ip = {}  # type: ignore[typeddict-item]
    if "IpAddress" in data:
        out["ip_address"] = data["IpAddress"]
    else:
        raise DeserializationError("Ip.ip_address required")
    return out
