"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationSpecificationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_reservation_preference
    import capo_ec2.types.capacity_reservation_target_response


class CapacityReservationSpecificationResponse(TypedDict, closed=True):
    capacity_reservation_preference: NotRequired[
        "capo_ec2.types.capacity_reservation_preference.CapacityReservationPreference"
    ]
    """<p>Describes the instance's Capacity Reservation preferences. Possible preferences include:</p> <ul> <li> <p> <code>open</code> - The instance can run in any <code>open</code> Capacity Reservation that has matching attributes (instance type, platform, Availability Zone).</p> </li> <li> <p> <code>none</code> - The instance avoids running in a Capacity Reservation even if one is available. The instance runs in On-Demand capacity.</p> </li> </ul>"""
    capacity_reservation_target: NotRequired[
        "capo_ec2.types.capacity_reservation_target_response.CapacityReservationTargetResponse"
    ]
    """<p>Information about the targeted Capacity Reservation or Capacity Reservation group.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityReservationSpecificationResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_reservation_preference" in value:
        import capo_ec2.types.capacity_reservation_preference

        capo_ec2.types.capacity_reservation_preference.serialize_ec2_query(
            value["capacity_reservation_preference"],
            pairs,
            f"{key_prefix}CapacityReservationPreference",
        )
    if "capacity_reservation_target" in value:
        import capo_ec2.types.capacity_reservation_target_response

        capo_ec2.types.capacity_reservation_target_response.serialize_ec2_query(
            value["capacity_reservation_target"],
            pairs,
            f"{key_prefix}CapacityReservationTarget",
        )


def deserialize_ec2_query(el: Element) -> CapacityReservationSpecificationResponse:
    out: CapacityReservationSpecificationResponse = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_preference = el.find("capacityReservationPreference")
    if child_capacity_reservation_preference is not None:
        import capo_ec2.types.capacity_reservation_preference

        out["capacity_reservation_preference"] = (
            capo_ec2.types.capacity_reservation_preference.deserialize_ec2_query(
                child_capacity_reservation_preference
            )
        )
    child_capacity_reservation_target = el.find("capacityReservationTarget")
    if child_capacity_reservation_target is not None:
        import capo_ec2.types.capacity_reservation_target_response

        out["capacity_reservation_target"] = (
            capo_ec2.types.capacity_reservation_target_response.deserialize_ec2_query(
                child_capacity_reservation_target
            )
        )
    return out
