"""Generated from Smithy shape ``com.amazonaws.ec2#InterruptionInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.interruption_type
    import aws_sdk_ec2.types.string


class InterruptionInfo(TypedDict):
    source_capacity_reservation_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The ID of the source Capacity Reservation from which the interruptible reservation was created. </p>"""
    interruption_type: NotRequired[
        "aws_sdk_ec2.types.interruption_type.InterruptionType"
    ]
    """<p> The interruption type that determines how instances are terminated when capacity is reclaimed. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InterruptionInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "source_capacity_reservation_id" in value:
        pairs.append(
            (
                f"{prefix}.SourceCapacityReservationId",
                str(value["source_capacity_reservation_id"]),
            )
        )
    if "interruption_type" in value:
        import aws_sdk_ec2.types.interruption_type

        aws_sdk_ec2.types.interruption_type.serialize_ec2_query(
            value["interruption_type"], pairs, f"{prefix}.InterruptionType"
        )


def deserialize_ec2_query(el: Element) -> InterruptionInfo:
    out: InterruptionInfo = {}  # type: ignore[typeddict-item]
    child_source_capacity_reservation_id = el.find("SourceCapacityReservationId")
    if child_source_capacity_reservation_id is not None:
        out["source_capacity_reservation_id"] = str(
            child_source_capacity_reservation_id.text or ""
        )
    child_interruption_type = el.find("InterruptionType")
    if child_interruption_type is not None:
        import aws_sdk_ec2.types.interruption_type

        out["interruption_type"] = (
            aws_sdk_ec2.types.interruption_type.deserialize_ec2_query(
                child_interruption_type
            )
        )
    return out
