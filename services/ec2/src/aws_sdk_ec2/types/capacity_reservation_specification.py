"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_preference
    import aws_sdk_ec2.types.capacity_reservation_target


class CapacityReservationSpecification(TypedDict):
    capacity_reservation_preference: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_preference.CapacityReservationPreference"
    ]
    """<p>Indicates the instance's Capacity Reservation preferences. Possible preferences include:</p> <ul> <li> <p> <code>capacity-reservations-only</code> - The instance will only run in a Capacity Reservation or Capacity Reservation group. If capacity isn't available, the instance will fail to launch.</p> </li> <li> <p> <code>open</code> - The instance can run in any <code>open</code> Capacity Reservation that has matching attributes (instance type, platform, Availability Zone, and tenancy). If capacity isn't available, the instance runs as an On-Demand Instance.</p> </li> <li> <p> <code>none</code> - The instance doesn't run in a Capacity Reservation even if one is available. The instance runs as an On-Demand Instance.</p> </li> </ul>"""
    capacity_reservation_target: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_target.CapacityReservationTarget"
    ]
    """<p>Information about the target Capacity Reservation or Capacity Reservation group.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityReservationSpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "capacity_reservation_preference" in value:
        import aws_sdk_ec2.types.capacity_reservation_preference

        aws_sdk_ec2.types.capacity_reservation_preference.serialize_ec2_query(
            value["capacity_reservation_preference"],
            pairs,
            f"{prefix}.CapacityReservationPreference",
        )
    if "capacity_reservation_target" in value:
        import aws_sdk_ec2.types.capacity_reservation_target

        aws_sdk_ec2.types.capacity_reservation_target.serialize_ec2_query(
            value["capacity_reservation_target"],
            pairs,
            f"{prefix}.CapacityReservationTarget",
        )


def deserialize_ec2_query(el: Element) -> CapacityReservationSpecification:
    out: CapacityReservationSpecification = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_preference = el.find("CapacityReservationPreference")
    if child_capacity_reservation_preference is not None:
        import aws_sdk_ec2.types.capacity_reservation_preference

        out["capacity_reservation_preference"] = (
            aws_sdk_ec2.types.capacity_reservation_preference.deserialize_ec2_query(
                child_capacity_reservation_preference
            )
        )
    child_capacity_reservation_target = el.find("CapacityReservationTarget")
    if child_capacity_reservation_target is not None:
        import aws_sdk_ec2.types.capacity_reservation_target

        out["capacity_reservation_target"] = (
            aws_sdk_ec2.types.capacity_reservation_target.deserialize_ec2_query(
                child_capacity_reservation_target
            )
        )
    return out
