"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityAllocationMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_allocation_metadata_entry

CapacityAllocationMetadataList: TypeAlias = list[
    "aws_sdk_ec2.types.capacity_allocation_metadata_entry.CapacityAllocationMetadataEntry"
]
