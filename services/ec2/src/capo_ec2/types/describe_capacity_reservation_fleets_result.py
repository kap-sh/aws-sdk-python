"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityReservationFleetsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_reservation_fleet_set
    import capo_ec2.types.string


class DescribeCapacityReservationFleetsResult(TypedDict, closed=True):
    capacity_reservation_fleets: NotRequired[
        "capo_ec2.types.capacity_reservation_fleet_set.CapacityReservationFleetSet"
    ]
    """<p>Information about the Capacity Reservation Fleets.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCapacityReservationFleetsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_reservation_fleets" in value:
        import capo_ec2.types.capacity_reservation_fleet_set

        capo_ec2.types.capacity_reservation_fleet_set.serialize_ec2_query(
            value["capacity_reservation_fleets"],
            pairs,
            f"{key_prefix}CapacityReservationFleetSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeCapacityReservationFleetsResult:
    out: DescribeCapacityReservationFleetsResult = {}  # type: ignore[typeddict-item]
    if el.find("capacityReservationFleetSet") is not None:
        import capo_ec2.types.capacity_reservation_fleet_set

        out["capacity_reservation_fleets"] = (
            capo_ec2.types.capacity_reservation_fleet_set.deserialize_ec2_query(
                el, "capacityReservationFleetSet"
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
