"""Generated from Smithy shape ``com.amazonaws.ec2#PurchaseCapacityBlockResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_block_set
    import aws_sdk_ec2.types.capacity_reservation


class PurchaseCapacityBlockResult(TypedDict, closed=True):
    capacity_reservation: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation.CapacityReservation"
    ]
    """<p>The Capacity Reservation.</p>"""
    capacity_blocks: NotRequired[
        "aws_sdk_ec2.types.capacity_block_set.CapacityBlockSet"
    ]
    """<p>The Capacity Block.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PurchaseCapacityBlockResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "capacity_reservation" in value:
        import aws_sdk_ec2.types.capacity_reservation

        aws_sdk_ec2.types.capacity_reservation.serialize_ec2_query(
            value["capacity_reservation"], pairs, f"{prefix}.CapacityReservation"
        )
    if "capacity_blocks" in value:
        import aws_sdk_ec2.types.capacity_block_set

        aws_sdk_ec2.types.capacity_block_set.serialize_ec2_query(
            value["capacity_blocks"], pairs, f"{prefix}.CapacityBlockSet"
        )


def deserialize_ec2_query(el: Element) -> PurchaseCapacityBlockResult:
    out: PurchaseCapacityBlockResult = {}  # type: ignore[typeddict-item]
    child_capacity_reservation = el.find("CapacityReservation")
    if child_capacity_reservation is not None:
        import aws_sdk_ec2.types.capacity_reservation

        out["capacity_reservation"] = (
            aws_sdk_ec2.types.capacity_reservation.deserialize_ec2_query(
                child_capacity_reservation
            )
        )
    if el.find("CapacityBlockSet") is not None:
        import aws_sdk_ec2.types.capacity_block_set

        out["capacity_blocks"] = (
            aws_sdk_ec2.types.capacity_block_set.deserialize_ec2_query(
                el, "CapacityBlockSet"
            )
        )
    return out
