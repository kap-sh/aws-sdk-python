"""Generated from Smithy shape ``com.amazonaws.securityhub#VpcInfoIpv6CidrBlockSetDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class VpcInfoIpv6CidrBlockSetDetails(TypedDict, closed=True):
    ipv6_cidr_block: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The IPv6 CIDR block for the VPC. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcInfoIpv6CidrBlockSetDetails) -> dict:
    out: dict = {}
    if "ipv6_cidr_block" in value:
        out["Ipv6CidrBlock"] = value["ipv6_cidr_block"]
    return out


def deserialize_json(data: dict) -> VpcInfoIpv6CidrBlockSetDetails:
    out: VpcInfoIpv6CidrBlockSetDetails = {}  # type: ignore[typeddict-item]
    if "Ipv6CidrBlock" in data:
        out["ipv6_cidr_block"] = data["Ipv6CidrBlock"]
    return out
