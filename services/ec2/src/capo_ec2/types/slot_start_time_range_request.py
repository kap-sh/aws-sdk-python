"""Generated from Smithy shape ``com.amazonaws.ec2#SlotStartTimeRangeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.date_time


class SlotStartTimeRangeRequest(TypedDict, closed=True):
    earliest_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The earliest date and time, in UTC, for the Scheduled Instance to start.</p>"""
    latest_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The latest date and time, in UTC, for the Scheduled Instance to start.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SlotStartTimeRangeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "earliest_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["earliest_time"], pairs, f"{key_prefix}EarliestTime"
        )
    if "latest_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["latest_time"], pairs, f"{key_prefix}LatestTime"
        )


def deserialize_ec2_query(el: Element) -> SlotStartTimeRangeRequest:
    out: SlotStartTimeRangeRequest = {}  # type: ignore[typeddict-item]
    child_earliest_time = el.find("EarliestTime")
    if child_earliest_time is not None:
        import capo_ec2.types.date_time

        out["earliest_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_earliest_time
        )
    child_latest_time = el.find("LatestTime")
    if child_latest_time is not None:
        import capo_ec2.types.date_time

        out["latest_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_latest_time
        )
    return out
