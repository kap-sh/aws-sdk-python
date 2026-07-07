"""Generated from Smithy shape ``com.amazonaws.panorama#EthernetPayload``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.connection_type
    import aws_sdk_panorama.types.static_ip_connection_info


class EthernetPayload(TypedDict, closed=True):
    connection_type: "aws_sdk_panorama.types.connection_type.ConnectionType"
    """<p>How the device gets an IP address.</p>"""
    static_ip_connection_info: NotRequired[
        "aws_sdk_panorama.types.static_ip_connection_info.StaticIpConnectionInfo"
    ]
    """<p>Network configuration for a static IP connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EthernetPayload) -> dict:
    out: dict = {}
    out["ConnectionType"] = value["connection_type"]
    if "static_ip_connection_info" in value:
        import aws_sdk_panorama.types.static_ip_connection_info

        out["StaticIpConnectionInfo"] = (
            aws_sdk_panorama.types.static_ip_connection_info.serialize_json(
                value["static_ip_connection_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> EthernetPayload:
    out: EthernetPayload = {}  # type: ignore[typeddict-item]
    if "ConnectionType" in data:
        out["connection_type"] = data["ConnectionType"]
    else:
        raise DeserializationError("EthernetPayload.connection_type required")
    if "StaticIpConnectionInfo" in data:
        import aws_sdk_panorama.types.static_ip_connection_info

        out["static_ip_connection_info"] = (
            aws_sdk_panorama.types.static_ip_connection_info.deserialize_json(
                data["StaticIpConnectionInfo"]
            )
        )
    return out
