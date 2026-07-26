"""Generated from Smithy shape ``com.amazonaws.autoscaling#CapacityReservationTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.capacity_reservation_ids
    import capo_auto_scaling.types.capacity_reservation_resource_group_arns


class CapacityReservationTarget(TypedDict, closed=True):
    capacity_reservation_ids: NotRequired[
        "capo_auto_scaling.types.capacity_reservation_ids.CapacityReservationIds"
    ]
    """<p> The Capacity Reservation IDs to launch instances into. </p>"""
    capacity_reservation_resource_group_arns: NotRequired[
        "capo_auto_scaling.types.capacity_reservation_resource_group_arns.CapacityReservationResourceGroupArns"
    ]
    """<p> The resource group ARNs of the Capacity Reservation to launch instances into. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CapacityReservationTarget, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "capacity_reservation_ids" in value:
        import capo_auto_scaling.types.capacity_reservation_ids

        capo_auto_scaling.types.capacity_reservation_ids.serialize_query(
            value["capacity_reservation_ids"], pairs, f"{prefix}.CapacityReservationIds"
        )
    if "capacity_reservation_resource_group_arns" in value:
        import capo_auto_scaling.types.capacity_reservation_resource_group_arns

        capo_auto_scaling.types.capacity_reservation_resource_group_arns.serialize_query(
            value["capacity_reservation_resource_group_arns"],
            pairs,
            f"{prefix}.CapacityReservationResourceGroupArns",
        )


def deserialize_query(el: Element) -> CapacityReservationTarget:
    out: CapacityReservationTarget = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_ids = el.find("CapacityReservationIds")
    if child_capacity_reservation_ids is not None:
        import capo_auto_scaling.types.capacity_reservation_ids

        out["capacity_reservation_ids"] = (
            capo_auto_scaling.types.capacity_reservation_ids.deserialize_query(
                child_capacity_reservation_ids
            )
        )
    child_capacity_reservation_resource_group_arns = el.find(
        "CapacityReservationResourceGroupArns"
    )
    if child_capacity_reservation_resource_group_arns is not None:
        import capo_auto_scaling.types.capacity_reservation_resource_group_arns

        out["capacity_reservation_resource_group_arns"] = (
            capo_auto_scaling.types.capacity_reservation_resource_group_arns.deserialize_query(
                child_capacity_reservation_resource_group_arns
            )
        )
    return out
