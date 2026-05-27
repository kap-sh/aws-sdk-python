"""Generated from Smithy shape ``com.amazonaws.ec2#GetReservedInstancesExchangeQuoteResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.reservation_value
    import aws_sdk_ec2.types.reserved_instance_reservation_value_set
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.target_reservation_value_set


class GetReservedInstancesExchangeQuoteResult(TypedDict):
    currency_code: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The currency of the transaction.</p>"""
    is_valid_exchange: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>If <code>true</code>, the exchange is valid. If <code>false</code>, the exchange cannot be completed.</p>"""
    output_reserved_instances_will_expire_at: NotRequired[
        "aws_sdk_ec2.types.date_time.DateTime"
    ]
    """<p>The new end date of the reservation term.</p>"""
    payment_due: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The total true upfront charge for the exchange.</p>"""
    reserved_instance_value_rollup: NotRequired[
        "aws_sdk_ec2.types.reservation_value.ReservationValue"
    ]
    """<p>The cost associated with the Reserved Instance.</p>"""
    reserved_instance_value_set: NotRequired[
        "aws_sdk_ec2.types.reserved_instance_reservation_value_set.ReservedInstanceReservationValueSet"
    ]
    """<p>The configuration of your Convertible Reserved Instances.</p>"""
    target_configuration_value_rollup: NotRequired[
        "aws_sdk_ec2.types.reservation_value.ReservationValue"
    ]
    """<p>The cost associated with the Reserved Instance.</p>"""
    target_configuration_value_set: NotRequired[
        "aws_sdk_ec2.types.target_reservation_value_set.TargetReservationValueSet"
    ]
    """<p>The values of the target Convertible Reserved Instances.</p>"""
    validation_failure_reason: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Describes the reason why the exchange cannot be completed.</p>"""
