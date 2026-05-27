"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityAllocation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.allocation_type
    import aws_sdk_ec2.types.capacity_allocation_metadata_list
    import aws_sdk_ec2.types.integer


class CapacityAllocation(TypedDict):
    allocation_type: NotRequired["aws_sdk_ec2.types.allocation_type.AllocationType"]
    """<p>The usage type. <code>used</code> indicates that the instance capacity is in use by instances that are running in the Capacity Reservation.</p>"""
    count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The amount of instance capacity associated with the usage. For example a value of <code>4</code> indicates that instance capacity for 4 instances is currently in use.</p>"""
    allocation_metadata: NotRequired[
        "aws_sdk_ec2.types.capacity_allocation_metadata_list.CapacityAllocationMetadataList"
    ]
    """<p>Additional metadata associated with the capacity allocation. Each entry contains a key-value pair providing context about the allocation.</p>"""
