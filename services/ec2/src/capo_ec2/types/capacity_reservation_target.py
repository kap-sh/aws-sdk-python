"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_reservation_id
    import capo_ec2.types.string


class CapacityReservationTarget(TypedDict, closed=True):
    capacity_reservation_id: NotRequired[
        "capo_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p>The ID of the Capacity Reservation in which to run the instance.</p>"""
    capacity_reservation_resource_group_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The ARN of the Capacity Reservation resource group in which to run the instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityReservationTarget, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "capacity_reservation_id" in value:
        pairs.append(
            (f"{prefix}.CapacityReservationId", str(value["capacity_reservation_id"]))
        )
    if "capacity_reservation_resource_group_arn" in value:
        pairs.append(
            (
                f"{prefix}.CapacityReservationResourceGroupArn",
                str(value["capacity_reservation_resource_group_arn"]),
            )
        )


def deserialize_ec2_query(el: Element) -> CapacityReservationTarget:
    out: CapacityReservationTarget = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_id = el.find("CapacityReservationId")
    if child_capacity_reservation_id is not None:
        out["capacity_reservation_id"] = str(child_capacity_reservation_id.text or "")
    child_capacity_reservation_resource_group_arn = el.find(
        "CapacityReservationResourceGroupArn"
    )
    if child_capacity_reservation_resource_group_arn is not None:
        out["capacity_reservation_resource_group_arn"] = str(
            child_capacity_reservation_resource_group_arn.text or ""
        )
    return out
