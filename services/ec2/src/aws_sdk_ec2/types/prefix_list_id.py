"""Generated from Smithy shape ``com.amazonaws.ec2#PrefixListId``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class PrefixListId(TypedDict):
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the security group rule that references this prefix list ID.</p> <p>Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*</p>"""
    prefix_list_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the prefix.</p>"""
