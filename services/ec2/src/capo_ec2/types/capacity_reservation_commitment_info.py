"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationCommitmentInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer
    import capo_ec2.types.millisecond_date_time


class CapacityReservationCommitmentInfo(TypedDict, closed=True):
    committed_instance_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The instance capacity that you committed to when you requested the future-dated Capacity Reservation.</p>"""
    commitment_end_date: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time at which the commitment duration expires, in the ISO8601 format in the UTC time zone (<code>YYYY-MM-DDThh:mm:ss.sssZ</code>). You can't decrease the instance count or cancel the Capacity Reservation before this date and time.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityReservationCommitmentInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "committed_instance_count" in value:
        pairs.append(
            (
                f"{key_prefix}CommittedInstanceCount",
                str(value["committed_instance_count"]),
            )
        )
    if "commitment_end_date" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["commitment_end_date"], pairs, f"{key_prefix}CommitmentEndDate"
        )


def deserialize_ec2_query(el: Element) -> CapacityReservationCommitmentInfo:
    out: CapacityReservationCommitmentInfo = {}  # type: ignore[typeddict-item]
    child_committed_instance_count = el.find("CommittedInstanceCount")
    if child_committed_instance_count is not None:
        out["committed_instance_count"] = int(child_committed_instance_count.text or "")
    child_commitment_end_date = el.find("CommitmentEndDate")
    if child_commitment_end_date is not None:
        import capo_ec2.types.millisecond_date_time

        out["commitment_end_date"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_commitment_end_date
            )
        )
    return out
