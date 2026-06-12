"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2SecurityGroupIpv6Range``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2SecurityGroupIpv6Range(TypedDict):
    cidr_ipv6: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The IPv6 CIDR range. You can specify either a CIDR range or a source security group, but not both. To specify a single IPv6 address, use the /128 prefix length.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2SecurityGroupIpv6Range) -> dict:
    out: dict = {}
    if "cidr_ipv6" in value:
        out["CidrIpv6"] = value["cidr_ipv6"]
    return out


def deserialize_json(data: dict) -> AwsEc2SecurityGroupIpv6Range:
    out: AwsEc2SecurityGroupIpv6Range = {}  # type: ignore[typeddict-item]
    if "CidrIpv6" in data:
        out["cidr_ipv6"] = data["CidrIpv6"]
    return out
