"""Generated from Smithy shape ``com.amazonaws.rds#RestoreWindow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.t_stamp


class RestoreWindow(TypedDict, closed=True):
    earliest_time: NotRequired["aws_sdk_rds.types.t_stamp.TStamp"]
    """<p>The earliest time you can restore an instance to.</p>"""
    latest_time: NotRequired["aws_sdk_rds.types.t_stamp.TStamp"]
    """<p>The latest time you can restore an instance to.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RestoreWindow, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "earliest_time" in value:
        import aws_sdk_rds.types.t_stamp

        aws_sdk_rds.types.t_stamp.serialize_query(
            value["earliest_time"], pairs, f"{prefix}.EarliestTime"
        )
    if "latest_time" in value:
        import aws_sdk_rds.types.t_stamp

        aws_sdk_rds.types.t_stamp.serialize_query(
            value["latest_time"], pairs, f"{prefix}.LatestTime"
        )


def deserialize_query(el: Element) -> RestoreWindow:
    out: RestoreWindow = {}  # type: ignore[typeddict-item]
    child_earliest_time = el.find("EarliestTime")
    if child_earliest_time is not None:
        import aws_sdk_rds.types.t_stamp

        out["earliest_time"] = aws_sdk_rds.types.t_stamp.deserialize_query(
            child_earliest_time
        )
    child_latest_time = el.find("LatestTime")
    if child_latest_time is not None:
        import aws_sdk_rds.types.t_stamp

        out["latest_time"] = aws_sdk_rds.types.t_stamp.deserialize_query(
            child_latest_time
        )
    return out
