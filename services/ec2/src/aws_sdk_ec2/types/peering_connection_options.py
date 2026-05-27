"""Generated from Smithy shape ``com.amazonaws.ec2#PeeringConnectionOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class PeeringConnectionOptions(TypedDict):
    allow_dns_resolution_from_remote_vpc: NotRequired[
        "aws_sdk_ec2.types.boolean.Boolean"
    ]
    """<p>If true, the public DNS hostnames of instances in the specified VPC resolve to private IP addresses when queried from instances in the peer VPC.</p>"""
    allow_egress_from_local_classic_link_to_remote_vpc: NotRequired[
        "aws_sdk_ec2.types.boolean.Boolean"
    ]
    """<p>Deprecated.</p>"""
    allow_egress_from_local_vpc_to_remote_classic_link: NotRequired[
        "aws_sdk_ec2.types.boolean.Boolean"
    ]
    """<p>Deprecated.</p>"""
