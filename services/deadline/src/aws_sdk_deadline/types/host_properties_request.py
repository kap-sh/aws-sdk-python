"""Generated from Smithy shape ``com.amazonaws.deadline#HostPropertiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.host_name
    import aws_sdk_deadline.types.ip_addresses


class HostPropertiesRequest(TypedDict, closed=True):
    ip_addresses: NotRequired["aws_sdk_deadline.types.ip_addresses.IpAddresses"]
    """<p>The IP address of the host.</p>"""
    host_name: NotRequired["aws_sdk_deadline.types.host_name.HostName"]
    """<p>The host name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HostPropertiesRequest) -> dict:
    out: dict = {}
    if "ip_addresses" in value:
        import aws_sdk_deadline.types.ip_addresses

        out["ipAddresses"] = aws_sdk_deadline.types.ip_addresses.serialize_json(
            value["ip_addresses"]
        )
    if "host_name" in value:
        out["hostName"] = value["host_name"]
    return out


def deserialize_json(data: dict) -> HostPropertiesRequest:
    out: HostPropertiesRequest = {}  # type: ignore[typeddict-item]
    if "ipAddresses" in data:
        import aws_sdk_deadline.types.ip_addresses

        out["ip_addresses"] = aws_sdk_deadline.types.ip_addresses.deserialize_json(
            data["ipAddresses"]
        )
    if "hostName" in data:
        out["host_name"] = data["hostName"]
    return out
