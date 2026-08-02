"""Generated from Smithy shape ``com.amazonaws.ec2#CancelCapacityReservationFleetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.capacity_reservation_fleet_id_set


class CancelCapacityReservationFleetsRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    capacity_reservation_fleet_ids: NotRequired[
        "capo_ec2.types.capacity_reservation_fleet_id_set.CapacityReservationFleetIdSet"
    ]
    """<p>The IDs of the Capacity Reservation Fleets to cancel.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CancelCapacityReservationFleetsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "capacity_reservation_fleet_ids" in value:
        import capo_ec2.types.capacity_reservation_fleet_id_set

        capo_ec2.types.capacity_reservation_fleet_id_set.serialize_ec2_query(
            value["capacity_reservation_fleet_ids"],
            pairs,
            f"{key_prefix}CapacityReservationFleetIds",
        )


def deserialize_ec2_query(el: Element) -> CancelCapacityReservationFleetsRequest:
    out: CancelCapacityReservationFleetsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("CapacityReservationFleetIds") is not None:
        import capo_ec2.types.capacity_reservation_fleet_id_set

        out["capacity_reservation_fleet_ids"] = (
            capo_ec2.types.capacity_reservation_fleet_id_set.deserialize_ec2_query(
                el, "CapacityReservationFleetIds"
            )
        )
    return out
