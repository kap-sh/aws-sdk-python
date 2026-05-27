"""Generated from Smithy shape ``com.amazonaws.ec2#RestoreManagedPrefixListVersionResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.managed_prefix_list


class RestoreManagedPrefixListVersionResult(TypedDict):
    prefix_list: NotRequired["aws_sdk_ec2.types.managed_prefix_list.ManagedPrefixList"]
    """<p>Information about the prefix list.</p>"""
