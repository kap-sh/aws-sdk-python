"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2SecurityGroupIpRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2SecurityGroupIpRange(TypedDict, closed=True):
    cidr_ip: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The IPv4 CIDR range. You can specify either a CIDR range or a source security group, but not both. To specify a single IPv4 address, use the /32 prefix length.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2SecurityGroupIpRange) -> dict:
    out: dict = {}
    if "cidr_ip" in value:
        out["CidrIp"] = value["cidr_ip"]
    return out


def deserialize_json(data: dict) -> AwsEc2SecurityGroupIpRange:
    out: AwsEc2SecurityGroupIpRange = {}  # type: ignore[typeddict-item]
    if "CidrIp" in data:
        out["cidr_ip"] = data["CidrIp"]
    return out
