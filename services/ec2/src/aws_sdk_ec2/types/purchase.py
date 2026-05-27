"""Generated from Smithy shape ``com.amazonaws.ec2#Purchase``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.currency_code_values
    import aws_sdk_ec2.types.host_reservation_id
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.payment_option
    import aws_sdk_ec2.types.response_host_id_set
    import aws_sdk_ec2.types.string


class Purchase(TypedDict):
    currency_code: NotRequired[
        "aws_sdk_ec2.types.currency_code_values.CurrencyCodeValues"
    ]
    """<p>The currency in which the <code>UpfrontPrice</code> and <code>HourlyPrice</code> amounts are specified. At this time, the only supported currency is <code>USD</code>.</p>"""
    duration: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The duration of the reservation's term in seconds.</p>"""
    host_id_set: NotRequired["aws_sdk_ec2.types.response_host_id_set.ResponseHostIdSet"]
    """<p>The IDs of the Dedicated Hosts associated with the reservation.</p>"""
    host_reservation_id: NotRequired[
        "aws_sdk_ec2.types.host_reservation_id.HostReservationId"
    ]
    """<p>The ID of the reservation.</p>"""
    hourly_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The hourly price of the reservation per hour.</p>"""
    instance_family: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The instance family on the Dedicated Host that the reservation can be associated with.</p>"""
    payment_option: NotRequired["aws_sdk_ec2.types.payment_option.PaymentOption"]
    """<p>The payment option for the reservation.</p>"""
    upfront_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The upfront price of the reservation.</p>"""
