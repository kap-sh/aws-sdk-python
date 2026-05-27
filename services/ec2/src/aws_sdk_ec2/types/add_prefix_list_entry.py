"""Generated from Smithy shape ``com.amazonaws.ec2#AddPrefixListEntry``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class AddPrefixListEntry(TypedDict):
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR block.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the entry.</p> <p>Constraints: Up to 255 characters in length.</p>"""
