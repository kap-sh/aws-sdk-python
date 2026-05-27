"""Generated from Smithy shape ``com.amazonaws.ec2#PrefixListEntry``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class PrefixListEntry(TypedDict):
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR block.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description.</p>"""
