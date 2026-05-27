"""Generated from Smithy shape ``com.amazonaws.ec2#HostReservation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.currency_code_values
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.host_reservation_id
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.offering_id
    import aws_sdk_ec2.types.payment_option
    import aws_sdk_ec2.types.reservation_state
    import aws_sdk_ec2.types.response_host_id_set
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class HostReservation(TypedDict):
    count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of Dedicated Hosts the reservation is associated with.</p>"""
    currency_code: NotRequired[
        "aws_sdk_ec2.types.currency_code_values.CurrencyCodeValues"
    ]
    """<p>The currency in which the <code>upfrontPrice</code> and <code>hourlyPrice</code> amounts are specified. At this time, the only supported currency is <code>USD</code>.</p>"""
    duration: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The length of the reservation's term, specified in seconds. Can be <code>31536000 (1 year)</code> | <code>94608000 (3 years)</code>.</p>"""
    end: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The date and time that the reservation ends.</p>"""
    host_id_set: NotRequired["aws_sdk_ec2.types.response_host_id_set.ResponseHostIdSet"]
    """<p>The IDs of the Dedicated Hosts associated with the reservation.</p>"""
    host_reservation_id: NotRequired[
        "aws_sdk_ec2.types.host_reservation_id.HostReservationId"
    ]
    """<p>The ID of the reservation that specifies the associated Dedicated Hosts.</p>"""
    hourly_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The hourly price of the reservation.</p>"""
    instance_family: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The instance family of the Dedicated Host Reservation. The instance family on the Dedicated Host must be the same in order for it to benefit from the reservation.</p>"""
    offering_id: NotRequired["aws_sdk_ec2.types.offering_id.OfferingId"]
    """<p>The ID of the reservation. This remains the same regardless of which Dedicated Hosts are associated with it.</p>"""
    payment_option: NotRequired["aws_sdk_ec2.types.payment_option.PaymentOption"]
    """<p>The payment option selected for this reservation.</p>"""
    start: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The date and time that the reservation started.</p>"""
    state: NotRequired["aws_sdk_ec2.types.reservation_state.ReservationState"]
    """<p>The state of the reservation.</p>"""
    upfront_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The upfront price of the reservation.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the Dedicated Host Reservation.</p>"""
