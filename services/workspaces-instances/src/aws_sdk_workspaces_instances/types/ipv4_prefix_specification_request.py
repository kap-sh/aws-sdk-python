"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#Ipv4PrefixSpecificationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.ipv4_prefix

class Ipv4PrefixSpecificationRequest(TypedDict):
    ipv4_prefix: NotRequired["aws_sdk_workspaces_instances.types.ipv4_prefix.Ipv4Prefix"]
    """<p>Specific IPv4 prefix for network interface configuration.</p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Ipv4PrefixSpecificationRequest) -> dict:
    out: dict = {}
    if "ipv4_prefix" in value:
        out["Ipv4Prefix"] = value["ipv4_prefix"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Ipv4PrefixSpecificationRequest:
    out: Ipv4PrefixSpecificationRequest = {}  # type: ignore[typeddict-item]
    if "Ipv4Prefix" in data:
        out["ipv4_prefix"] = data["Ipv4Prefix"]
    return out