"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolverVersionEntrySet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_version_entry

IpamPrefixListResolverVersionEntrySet: TypeAlias = list[
    "aws_sdk_ec2.types.ipam_prefix_list_resolver_version_entry.IpamPrefixListResolverVersionEntry"
]
