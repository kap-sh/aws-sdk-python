"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityBlock``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_block_id
    import aws_sdk_ec2.types.capacity_block_resource_state
    import aws_sdk_ec2.types.capacity_reservation_id_set
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class CapacityBlock(TypedDict):
    capacity_block_id: NotRequired[
        "aws_sdk_ec2.types.capacity_block_id.CapacityBlockId"
    ]
    """<p>The ID of the Capacity Block.</p>"""
    ultraserver_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The EC2 UltraServer type of the Capacity Block.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone of the Capacity Block.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone ID of the Capacity Block.</p>"""
    capacity_reservation_ids: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_id_set.CapacityReservationIdSet"
    ]
    """<p>The ID of the Capacity Reservation.</p>"""
    start_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time at which the Capacity Block was started.</p>"""
    end_date: NotRequired["aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The date and time at which the Capacity Block expires. When a Capacity Block expires, all instances in the Capacity Block are terminated.</p>"""
    create_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time at which the Capacity Block was created.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.capacity_block_resource_state.CapacityBlockResourceState"
    ]
    """<p>The state of the Capacity Block.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the Capacity Block.</p>"""
