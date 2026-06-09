"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityReservationTopologyResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_topology_set
    import aws_sdk_ec2.types.string


class DescribeCapacityReservationTopologyResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    capacity_reservations: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_topology_set.CapacityReservationTopologySet"
    ]
    """<p>Information about the topology of each Capacity Reservation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCapacityReservationTopologyResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "capacity_reservations" in value:
        import aws_sdk_ec2.types.capacity_reservation_topology_set

        aws_sdk_ec2.types.capacity_reservation_topology_set.serialize_ec2_query(
            value["capacity_reservations"], pairs, f"{prefix}.CapacityReservationSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeCapacityReservationTopologyResult:
    out: DescribeCapacityReservationTopologyResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("CapacityReservationSet") is not None:
        import aws_sdk_ec2.types.capacity_reservation_topology_set

        out["capacity_reservations"] = (
            aws_sdk_ec2.types.capacity_reservation_topology_set.deserialize_ec2_query(
                el, "CapacityReservationSet"
            )
        )
    return out
