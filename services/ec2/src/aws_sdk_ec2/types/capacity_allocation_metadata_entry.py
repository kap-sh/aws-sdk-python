"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityAllocationMetadataEntry``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class CapacityAllocationMetadataEntry(TypedDict):
    key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The key of the metadata entry.</p>"""
    value: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The value of the metadata entry.</p>"""
