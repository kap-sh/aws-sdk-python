"""Generated from Smithy shape ``com.amazonaws.ec2#ImageAncestryEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_ancestry_entry

ImageAncestryEntryList: TypeAlias = list[
    "aws_sdk_ec2.types.image_ancestry_entry.ImageAncestryEntry"
]
