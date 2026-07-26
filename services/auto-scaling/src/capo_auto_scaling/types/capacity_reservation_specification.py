"""Generated from Smithy shape ``com.amazonaws.autoscaling#CapacityReservationSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.capacity_reservation_preference
    import capo_auto_scaling.types.capacity_reservation_target


class CapacityReservationSpecification(TypedDict, closed=True):
    capacity_reservation_preference: NotRequired[
        "capo_auto_scaling.types.capacity_reservation_preference.CapacityReservationPreference"
    ]
    """<p> The capacity reservation preference. The following options are available: </p> <ul> <li> <p> <code>capacity-reservations-only</code> - Auto Scaling will only launch instances into a Capacity Reservation or Capacity Reservation resource group. If capacity isn't available, instances will fail to launch.</p> </li> <li> <p> <code>capacity-reservations-first</code> - Auto Scaling will try to launch instances into a Capacity Reservation or Capacity Reservation resource group first. If capacity isn't available, instances will run in On-Demand capacity.</p> </li> <li> <p> <code>none</code> - Auto Scaling will not launch instances into a Capacity Reservation. Instances will run in On-Demand capacity. </p> </li> <li> <p> <code>default</code> - Auto Scaling uses the Capacity Reservation preference from your launch template or an open Capacity Reservation.</p> </li> </ul>"""
    capacity_reservation_target: NotRequired[
        "capo_auto_scaling.types.capacity_reservation_target.CapacityReservationTarget"
    ]
    """<p> Describes a target Capacity Reservation or Capacity Reservation resource group. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CapacityReservationSpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "capacity_reservation_preference" in value:
        import capo_auto_scaling.types.capacity_reservation_preference

        capo_auto_scaling.types.capacity_reservation_preference.serialize_query(
            value["capacity_reservation_preference"],
            pairs,
            f"{prefix}.CapacityReservationPreference",
        )
    if "capacity_reservation_target" in value:
        import capo_auto_scaling.types.capacity_reservation_target

        capo_auto_scaling.types.capacity_reservation_target.serialize_query(
            value["capacity_reservation_target"],
            pairs,
            f"{prefix}.CapacityReservationTarget",
        )


def deserialize_query(el: Element) -> CapacityReservationSpecification:
    out: CapacityReservationSpecification = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_preference = el.find("CapacityReservationPreference")
    if child_capacity_reservation_preference is not None:
        import capo_auto_scaling.types.capacity_reservation_preference

        out["capacity_reservation_preference"] = (
            capo_auto_scaling.types.capacity_reservation_preference.deserialize_query(
                child_capacity_reservation_preference
            )
        )
    child_capacity_reservation_target = el.find("CapacityReservationTarget")
    if child_capacity_reservation_target is not None:
        import capo_auto_scaling.types.capacity_reservation_target

        out["capacity_reservation_target"] = (
            capo_auto_scaling.types.capacity_reservation_target.deserialize_query(
                child_capacity_reservation_target
            )
        )
    return out
