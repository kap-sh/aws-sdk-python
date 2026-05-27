"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityBlockExtensionOffering``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.availability_zone_name
    import aws_sdk_ec2.types.capacity_reservation_tenancy
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.offering_id
    import aws_sdk_ec2.types.string


class CapacityBlockExtensionOffering(TypedDict):
    capacity_block_extension_offering_id: NotRequired[
        "aws_sdk_ec2.types.offering_id.OfferingId"
    ]
    """<p>The ID of the Capacity Block extension offering.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The instance type of the Capacity Block that will be extended.</p>"""
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of instances in the Capacity Block extension offering.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_ec2.types.availability_zone_name.AvailabilityZoneName"
    ]
    """<p>The Availability Zone of the Capacity Block that will be extended.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The Availability Zone ID of the Capacity Block that will be extended.</p>"""
    start_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The start date of the Capacity Block that will be extended.</p>"""
    capacity_block_extension_start_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time at which the Capacity Block extension will start. This date is also the same as the end date of the Capacity Block that will be extended.</p>"""
    capacity_block_extension_end_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time at which the Capacity Block extension expires. When a Capacity Block expires, the reserved capacity is released and you can no longer launch instances into it. The Capacity Block's state changes to <code>expired</code> when it reaches its end date</p>"""
    capacity_block_extension_duration_hours: NotRequired[
        "aws_sdk_ec2.types.integer.Integer"
    ]
    """<p>The amount of time of the Capacity Block extension offering in hours.</p>"""
    upfront_fee: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The total price of the Capacity Block extension offering, to be paid up front.</p>"""
    currency_code: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The currency of the payment for the Capacity Block extension offering.</p>"""
    tenancy: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_tenancy.CapacityReservationTenancy"
    ]
    """<p>Indicates the tenancy of the Capacity Block extension offering. A Capacity Block can have one of the following tenancy settings:</p> <ul> <li> <p> <code>default</code> - The Capacity Block is created on hardware that is shared with other Amazon Web Services accounts.</p> </li> <li> <p> <code>dedicated</code> - The Capacity Block is created on single-tenant hardware that is dedicated to a single Amazon Web Services account.</p> </li> </ul>"""
    zone_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of zone where the Capacity Block extension offering is available.</p>"""
