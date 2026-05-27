"""Generated from Smithy shape ``com.amazonaws.ec2#TargetReservationValue``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reservation_value
    import aws_sdk_ec2.types.target_configuration


class TargetReservationValue(TypedDict):
    reservation_value: NotRequired[
        "aws_sdk_ec2.types.reservation_value.ReservationValue"
    ]
    """<p>The total value of the Convertible Reserved Instances that make up the exchange. This is the sum of the list value, remaining upfront price, and additional upfront cost of the exchange.</p>"""
    target_configuration: NotRequired[
        "aws_sdk_ec2.types.target_configuration.TargetConfiguration"
    ]
    """<p>The configuration of the Convertible Reserved Instances that make up the exchange.</p>"""
