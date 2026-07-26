"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#PrivateIpAddressSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.ipv4_address


class PrivateIpAddressSpecification(TypedDict, closed=True):
    primary: NotRequired["bool"]
    """<p>Indicates if this is the primary private IP address.</p>"""
    private_ip_address: NotRequired[
        "capo_workspaces_instances.types.ipv4_address.Ipv4Address"
    ]
    """<p>Specific private IP address for the network interface.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PrivateIpAddressSpecification) -> dict:
    out: dict = {}
    if "primary" in value:
        out["Primary"] = value["primary"]
    if "private_ip_address" in value:
        out["PrivateIpAddress"] = value["private_ip_address"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PrivateIpAddressSpecification:
    out: PrivateIpAddressSpecification = {}  # type: ignore[typeddict-item]
    if "Primary" in data:
        out["primary"] = data["Primary"]
    if "PrivateIpAddress" in data:
        out["private_ip_address"] = data["PrivateIpAddress"]
    return out
