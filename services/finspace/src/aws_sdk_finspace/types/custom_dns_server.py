"""Generated from Smithy shape ``com.amazonaws.finspace#CustomDNSServer``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_finspace.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_finspace.types.valid_hostname
    import aws_sdk_finspace.types.valid_ip_address


class CustomDNSServer(TypedDict, closed=True):
    custom_dns_server_name: "aws_sdk_finspace.types.valid_hostname.ValidHostname"
    """<p>The name of the DNS server.</p>"""
    custom_dns_server_ip: "aws_sdk_finspace.types.valid_ip_address.ValidIPAddress"
    """<p>The IP address of the DNS server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomDNSServer) -> dict:
    out: dict = {}
    out["customDNSServerName"] = value["custom_dns_server_name"]
    out["customDNSServerIP"] = value["custom_dns_server_ip"]
    return out


def deserialize_json(data: dict) -> CustomDNSServer:
    out: CustomDNSServer = {}  # type: ignore[typeddict-item]
    if "customDNSServerName" in data:
        out["custom_dns_server_name"] = data["customDNSServerName"]
    else:
        raise DeserializationError("CustomDNSServer.custom_dns_server_name required")
    if "customDNSServerIP" in data:
        out["custom_dns_server_ip"] = data["customDNSServerIP"]
    else:
        raise DeserializationError("CustomDNSServer.custom_dns_server_ip required")
    return out
