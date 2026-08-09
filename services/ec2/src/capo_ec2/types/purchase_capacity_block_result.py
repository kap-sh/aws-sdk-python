"""Generated from Smithy shape ``com.amazonaws.ec2#PurchaseCapacityBlockResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_block_set
    import capo_ec2.types.capacity_reservation


class PurchaseCapacityBlockResult(TypedDict, closed=True):
    capacity_reservation: NotRequired[
        "capo_ec2.types.capacity_reservation.CapacityReservation"
    ]
    """<p>The Capacity Reservation.</p>"""
    capacity_blocks: NotRequired["capo_ec2.types.capacity_block_set.CapacityBlockSet"]
    """<p>The Capacity Block.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PurchaseCapacityBlockResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_reservation" in value:
        import capo_ec2.types.capacity_reservation

        capo_ec2.types.capacity_reservation.serialize_ec2_query(
            value["capacity_reservation"], pairs, f"{key_prefix}CapacityReservation"
        )
    if "capacity_blocks" in value:
        import capo_ec2.types.capacity_block_set

        capo_ec2.types.capacity_block_set.serialize_ec2_query(
            value["capacity_blocks"], pairs, f"{key_prefix}CapacityBlockSet"
        )


def deserialize_ec2_query(el: Element) -> PurchaseCapacityBlockResult:
    out: PurchaseCapacityBlockResult = {}  # type: ignore[typeddict-item]
    child_capacity_reservation = el.find("capacityReservation")
    if child_capacity_reservation is not None:
        import capo_ec2.types.capacity_reservation

        out["capacity_reservation"] = (
            capo_ec2.types.capacity_reservation.deserialize_ec2_query(
                child_capacity_reservation
            )
        )
    child_capacity_blocks = el.find("capacityBlockSet")
    if child_capacity_blocks is not None:
        import capo_ec2.types.capacity_block_set

        out["capacity_blocks"] = (
            capo_ec2.types.capacity_block_set.deserialize_ec2_query(
                child_capacity_blocks
            )
        )
    return out
