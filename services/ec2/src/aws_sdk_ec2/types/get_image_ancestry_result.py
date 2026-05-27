"""Generated from Smithy shape ``com.amazonaws.ec2#GetImageAncestryResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_ancestry_entry_list


class GetImageAncestryResult(TypedDict):
    image_ancestry_entries: NotRequired[
        "aws_sdk_ec2.types.image_ancestry_entry_list.ImageAncestryEntryList"
    ]
    """<p>A list of entries in the AMI ancestry chain, from the specified AMI to the root AMI.</p>"""
