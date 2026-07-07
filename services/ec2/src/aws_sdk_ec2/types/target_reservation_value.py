"""Generated from Smithy shape ``com.amazonaws.ec2#TargetReservationValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reservation_value
    import aws_sdk_ec2.types.target_configuration


class TargetReservationValue(TypedDict, closed=True):
    reservation_value: NotRequired[
        "aws_sdk_ec2.types.reservation_value.ReservationValue"
    ]
    """<p>The total value of the Convertible Reserved Instances that make up the exchange. This is the sum of the list value, remaining upfront price, and additional upfront cost of the exchange.</p>"""
    target_configuration: NotRequired[
        "aws_sdk_ec2.types.target_configuration.TargetConfiguration"
    ]
    """<p>The configuration of the Convertible Reserved Instances that make up the exchange.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TargetReservationValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "reservation_value" in value:
        import aws_sdk_ec2.types.reservation_value

        aws_sdk_ec2.types.reservation_value.serialize_ec2_query(
            value["reservation_value"], pairs, f"{prefix}.ReservationValue"
        )
    if "target_configuration" in value:
        import aws_sdk_ec2.types.target_configuration

        aws_sdk_ec2.types.target_configuration.serialize_ec2_query(
            value["target_configuration"], pairs, f"{prefix}.TargetConfiguration"
        )


def deserialize_ec2_query(el: Element) -> TargetReservationValue:
    out: TargetReservationValue = {}  # type: ignore[typeddict-item]
    child_reservation_value = el.find("ReservationValue")
    if child_reservation_value is not None:
        import aws_sdk_ec2.types.reservation_value

        out["reservation_value"] = (
            aws_sdk_ec2.types.reservation_value.deserialize_ec2_query(
                child_reservation_value
            )
        )
    child_target_configuration = el.find("TargetConfiguration")
    if child_target_configuration is not None:
        import aws_sdk_ec2.types.target_configuration

        out["target_configuration"] = (
            aws_sdk_ec2.types.target_configuration.deserialize_ec2_query(
                child_target_configuration
            )
        )
    return out
