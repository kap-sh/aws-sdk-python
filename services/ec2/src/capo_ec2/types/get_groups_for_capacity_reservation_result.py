"""Generated from Smithy shape ``com.amazonaws.ec2#GetGroupsForCapacityReservationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_reservation_group_set
    import capo_ec2.types.string


class GetGroupsForCapacityReservationResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    capacity_reservation_groups: NotRequired[
        "capo_ec2.types.capacity_reservation_group_set.CapacityReservationGroupSet"
    ]
    """<p>Information about the resource groups to which the Capacity Reservation has been added.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetGroupsForCapacityReservationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "capacity_reservation_groups" in value:
        import capo_ec2.types.capacity_reservation_group_set

        capo_ec2.types.capacity_reservation_group_set.serialize_ec2_query(
            value["capacity_reservation_groups"],
            pairs,
            f"{key_prefix}CapacityReservationGroupSet",
        )


def deserialize_ec2_query(el: Element) -> GetGroupsForCapacityReservationResult:
    out: GetGroupsForCapacityReservationResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("capacityReservationGroupSet") is not None:
        import capo_ec2.types.capacity_reservation_group_set

        out["capacity_reservation_groups"] = (
            capo_ec2.types.capacity_reservation_group_set.deserialize_ec2_query(
                el, "capacityReservationGroupSet"
            )
        )
    return out
