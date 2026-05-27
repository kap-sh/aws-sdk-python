"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamPrefixListResolverResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_prefix_list_resolver


class ModifyIpamPrefixListResolverResult(TypedDict):
    ipam_prefix_list_resolver: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver.IpamPrefixListResolver"
    ]
    """<p>Information about the modified IPAM prefix list resolver.</p>"""
