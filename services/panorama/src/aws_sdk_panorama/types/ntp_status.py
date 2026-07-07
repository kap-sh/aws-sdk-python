"""Generated from Smithy shape ``com.amazonaws.panorama#NtpStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_panorama.types.ip_address
    import aws_sdk_panorama.types.network_connection_status
    import aws_sdk_panorama.types.ntp_server_name


class NtpStatus(TypedDict, closed=True):
    connection_status: NotRequired[
        "aws_sdk_panorama.types.network_connection_status.NetworkConnectionStatus"
    ]
    """<p>The connection's status.</p>"""
    ip_address: NotRequired["aws_sdk_panorama.types.ip_address.IpAddress"]
    """<p>The IP address of the server.</p>"""
    ntp_server_name: NotRequired["aws_sdk_panorama.types.ntp_server_name.NtpServerName"]
    """<p>The domain name of the server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NtpStatus) -> dict:
    out: dict = {}
    if "connection_status" in value:
        out["ConnectionStatus"] = value["connection_status"]
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "ntp_server_name" in value:
        out["NtpServerName"] = value["ntp_server_name"]
    return out


def deserialize_json(data: dict) -> NtpStatus:
    out: NtpStatus = {}  # type: ignore[typeddict-item]
    if "ConnectionStatus" in data:
        out["connection_status"] = data["ConnectionStatus"]
    if "IpAddress" in data:
        out["ip_address"] = data["IpAddress"]
    if "NtpServerName" in data:
        out["ntp_server_name"] = data["NtpServerName"]
    return out
