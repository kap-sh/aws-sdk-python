"""Generated from Smithy shape ``com.amazonaws.securityhub#VpcInfoPeeringOptionsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean


class VpcInfoPeeringOptionsDetails(TypedDict, closed=True):
    allow_dns_resolution_from_remote_vpc: NotRequired[
        "aws_sdk_securityhub.types.boolean.Boolean"
    ]
    """<p>Indicates whether a local VPC can resolve public DNS hostnames to private IP addresses when queried from instances in a peer VPC. </p>"""
    allow_egress_from_local_classic_link_to_remote_vpc: NotRequired[
        "aws_sdk_securityhub.types.boolean.Boolean"
    ]
    """<p>Indicates whether a local ClassicLink connection can communicate with the peer VPC over the VPC peering connection. </p>"""
    allow_egress_from_local_vpc_to_remote_classic_link: NotRequired[
        "aws_sdk_securityhub.types.boolean.Boolean"
    ]
    """<p>Indicates whether a local VPC can communicate with a ClassicLink connection in the peer VPC over the VPC peering connection. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcInfoPeeringOptionsDetails) -> dict:
    out: dict = {}
    if "allow_dns_resolution_from_remote_vpc" in value:
        out["AllowDnsResolutionFromRemoteVpc"] = value[
            "allow_dns_resolution_from_remote_vpc"
        ]
    if "allow_egress_from_local_classic_link_to_remote_vpc" in value:
        out["AllowEgressFromLocalClassicLinkToRemoteVpc"] = value[
            "allow_egress_from_local_classic_link_to_remote_vpc"
        ]
    if "allow_egress_from_local_vpc_to_remote_classic_link" in value:
        out["AllowEgressFromLocalVpcToRemoteClassicLink"] = value[
            "allow_egress_from_local_vpc_to_remote_classic_link"
        ]
    return out


def deserialize_json(data: dict) -> VpcInfoPeeringOptionsDetails:
    out: VpcInfoPeeringOptionsDetails = {}  # type: ignore[typeddict-item]
    if "AllowDnsResolutionFromRemoteVpc" in data:
        out["allow_dns_resolution_from_remote_vpc"] = data[
            "AllowDnsResolutionFromRemoteVpc"
        ]
    if "AllowEgressFromLocalClassicLinkToRemoteVpc" in data:
        out["allow_egress_from_local_classic_link_to_remote_vpc"] = data[
            "AllowEgressFromLocalClassicLinkToRemoteVpc"
        ]
    if "AllowEgressFromLocalVpcToRemoteClassicLink" in data:
        out["allow_egress_from_local_vpc_to_remote_classic_link"] = data[
            "AllowEgressFromLocalVpcToRemoteClassicLink"
        ]
    return out
