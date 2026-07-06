"""Generated from Smithy shape ``com.amazonaws.appmesh#DnsServiceDiscovery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.dns_response_type
    import aws_sdk_app_mesh.types.hostname
    import aws_sdk_app_mesh.types.ip_preference


class DnsServiceDiscovery(TypedDict, closed=True):
    hostname: "aws_sdk_app_mesh.types.hostname.Hostname"
    """<p>Specifies the DNS service discovery hostname for the virtual node. </p>"""
    response_type: NotRequired[
        "aws_sdk_app_mesh.types.dns_response_type.DnsResponseType"
    ]
    """<p>Specifies the DNS response type for the virtual node.</p>"""
    ip_preference: NotRequired["aws_sdk_app_mesh.types.ip_preference.IpPreference"]
    """<p>The preferred IP version that this virtual node uses. Setting the IP preference on the virtual node only overrides the IP preference set for the mesh on this specific node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DnsServiceDiscovery) -> dict:
    out: dict = {}
    out["hostname"] = value["hostname"]
    if "response_type" in value:
        out["responseType"] = value["response_type"]
    if "ip_preference" in value:
        out["ipPreference"] = value["ip_preference"]
    return out


def deserialize_json(data: dict) -> DnsServiceDiscovery:
    out: DnsServiceDiscovery = {}  # type: ignore[typeddict-item]
    if "hostname" in data:
        out["hostname"] = data["hostname"]
    else:
        raise DeserializationError("DnsServiceDiscovery.hostname required")
    if "responseType" in data:
        out["response_type"] = data["responseType"]
    if "ipPreference" in data:
        out["ip_preference"] = data["ipPreference"]
    return out
