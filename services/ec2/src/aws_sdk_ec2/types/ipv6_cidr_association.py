"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv6CidrAssociation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class Ipv6CidrAssociation(TypedDict):
    ipv6_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 CIDR block.</p>"""
    associated_resource: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The resource that's associated with the IPv6 CIDR block.</p>"""
