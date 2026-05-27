"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityBlockExtension``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.availability_zone_name
    import aws_sdk_ec2.types.capacity_block_extension_status
    import aws_sdk_ec2.types.capacity_reservation_id
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.offering_id
    import aws_sdk_ec2.types.string


class CapacityBlockExtension(TypedDict):
    capacity_reservation_id: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p>The reservation ID of the Capacity Block extension.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The instance type of the Capacity Block extension.</p>"""
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of instances in the Capacity Block extension.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_ec2.types.availability_zone_name.AvailabilityZoneName"
    ]
    """<p>The Availability Zone of the Capacity Block extension.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The Availability Zone ID of the Capacity Block extension.</p>"""
    capacity_block_extension_offering_id: NotRequired[
        "aws_sdk_ec2.types.offering_id.OfferingId"
    ]
    """<p>The ID of the Capacity Block extension offering.</p>"""
    capacity_block_extension_duration_hours: NotRequired[
        "aws_sdk_ec2.types.integer.Integer"
    ]
    """<p>The duration of the Capacity Block extension in hours.</p>"""
    capacity_block_extension_status: NotRequired[
        "aws_sdk_ec2.types.capacity_block_extension_status.CapacityBlockExtensionStatus"
    ]
    """<p>The status of the Capacity Block extension. A Capacity Block extension can have one of the following statuses:</p> <ul> <li> <p> <code>payment-pending</code> - The Capacity Block extension payment is processing. If your payment can't be processed within 12 hours, the Capacity Block extension is failed.</p> </li> <li> <p> <code>payment-failed</code> - Payment for the Capacity Block extension request was not successful.</p> </li> <li> <p> <code>payment-succeeded</code> - Payment for the Capacity Block extension request was successful. You receive an invoice that reflects the one-time upfront payment. In the invoice, you can associate the paid amount with the Capacity Block reservation ID.</p> </li> </ul>"""
    capacity_block_extension_purchase_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date when the Capacity Block extension was purchased.</p>"""
    capacity_block_extension_start_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The start date of the Capacity Block extension.</p>"""
    capacity_block_extension_end_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The end date of the Capacity Block extension.</p>"""
    upfront_fee: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The total price to be paid up front.</p>"""
    currency_code: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The currency of the payment for the Capacity Block extension.</p>"""
    zone_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of zone where the Capacity Block extension is located.</p>"""
