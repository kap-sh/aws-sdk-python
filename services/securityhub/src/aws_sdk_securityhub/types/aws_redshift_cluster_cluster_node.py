"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRedshiftClusterClusterNode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsRedshiftClusterClusterNode(TypedDict, closed=True):
    node_role: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The role of the node. A node might be a leader node or a compute node.</p>"""
    private_ip_address: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The private IP address of the node.</p>"""
    public_ip_address: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The public IP address of the node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRedshiftClusterClusterNode) -> dict:
    out: dict = {}
    if "node_role" in value:
        out["NodeRole"] = value["node_role"]
    if "private_ip_address" in value:
        out["PrivateIpAddress"] = value["private_ip_address"]
    if "public_ip_address" in value:
        out["PublicIpAddress"] = value["public_ip_address"]
    return out


def deserialize_json(data: dict) -> AwsRedshiftClusterClusterNode:
    out: AwsRedshiftClusterClusterNode = {}  # type: ignore[typeddict-item]
    if "NodeRole" in data:
        out["node_role"] = data["NodeRole"]
    if "PrivateIpAddress" in data:
        out["private_ip_address"] = data["PrivateIpAddress"]
    if "PublicIpAddress" in data:
        out["public_ip_address"] = data["PublicIpAddress"]
    return out
