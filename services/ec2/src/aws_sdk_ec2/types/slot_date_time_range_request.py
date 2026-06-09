"""Generated from Smithy shape ``com.amazonaws.ec2#SlotDateTimeRangeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time


class SlotDateTimeRangeRequest(TypedDict):
    earliest_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The earliest date and time, in UTC, for the Scheduled Instance to start.</p>"""
    latest_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The latest date and time, in UTC, for the Scheduled Instance to start. This value must be later than or equal to the earliest date and at most three months in the future.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SlotDateTimeRangeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "earliest_time" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["earliest_time"], pairs, f"{prefix}.EarliestTime"
        )
    if "latest_time" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["latest_time"], pairs, f"{prefix}.LatestTime"
        )


def deserialize_ec2_query(el: Element) -> SlotDateTimeRangeRequest:
    out: SlotDateTimeRangeRequest = {}  # type: ignore[typeddict-item]
    child_earliest_time = el.find("EarliestTime")
    if child_earliest_time is not None:
        import aws_sdk_ec2.types.date_time

        out["earliest_time"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_earliest_time
        )
    child_latest_time = el.find("LatestTime")
    if child_latest_time is not None:
        import aws_sdk_ec2.types.date_time

        out["latest_time"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_latest_time
        )
    return out
