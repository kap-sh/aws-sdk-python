"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolverVersion``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.long


class IpamPrefixListResolverVersion(TypedDict):
    version: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The version number of the IPAM prefix list resolver.</p> <p>Each version is a snapshot of what CIDRs matched your rules at that moment in time. The version number increments every time the CIDR list changes due to infrastructure changes.</p>"""
