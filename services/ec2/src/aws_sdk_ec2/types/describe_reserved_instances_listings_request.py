"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeReservedInstancesListingsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.reservation_id
    import aws_sdk_ec2.types.reserved_instances_listing_id


class DescribeReservedInstancesListingsRequest(TypedDict):
    reserved_instances_id: NotRequired["aws_sdk_ec2.types.reservation_id.ReservationId"]
    """<p>One or more Reserved Instance IDs.</p>"""
    reserved_instances_listing_id: NotRequired[
        "aws_sdk_ec2.types.reserved_instances_listing_id.ReservedInstancesListingId"
    ]
    """<p>One or more Reserved Instance listing IDs.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>reserved-instances-id</code> - The ID of the Reserved Instances.</p> </li> <li> <p> <code>reserved-instances-listing-id</code> - The ID of the Reserved Instances listing.</p> </li> <li> <p> <code>status</code> - The status of the Reserved Instance listing (<code>pending</code> | <code>active</code> | <code>cancelled</code> | <code>closed</code>).</p> </li> <li> <p> <code>status-message</code> - The reason for the status.</p> </li> </ul>"""
