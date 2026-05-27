"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamPrefixListResolverTargetResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_target


class ModifyIpamPrefixListResolverTargetResult(TypedDict):
    ipam_prefix_list_resolver_target: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_target.IpamPrefixListResolverTarget"
    ]
    """<p>Information about the modified IPAM prefix list resolver target.</p>"""
