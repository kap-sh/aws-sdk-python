"""Generated from Smithy shape ``com.amazonaws.ec2#InterruptionInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.interruption_type
    import capo_ec2.types.string


class InterruptionInfo(TypedDict, closed=True):
    source_capacity_reservation_id: NotRequired["capo_ec2.types.string.String"]
    """<p> The ID of the source Capacity Reservation from which the interruptible reservation was created. </p>"""
    interruption_type: NotRequired["capo_ec2.types.interruption_type.InterruptionType"]
    """<p> The interruption type that determines how instances are terminated when capacity is reclaimed. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InterruptionInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "source_capacity_reservation_id" in value:
        pairs.append(
            (
                f"{key_prefix}SourceCapacityReservationId",
                str(value["source_capacity_reservation_id"]),
            )
        )
    if "interruption_type" in value:
        import capo_ec2.types.interruption_type

        capo_ec2.types.interruption_type.serialize_ec2_query(
            value["interruption_type"], pairs, f"{key_prefix}InterruptionType"
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
        import capo_ec2.types.interruption_type

        out["interruption_type"] = (
            capo_ec2.types.interruption_type.deserialize_ec2_query(
                child_interruption_type
            )
        )
    return out
