"""Generated from Smithy shape ``com.amazonaws.elasticache#TimeRangeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.t_stamp


class TimeRangeFilter(TypedDict, closed=True):
    start_time: NotRequired["aws_sdk_elasticache.types.t_stamp.TStamp"]
    """<p>The start time of the time range filter</p>"""
    end_time: NotRequired["aws_sdk_elasticache.types.t_stamp.TStamp"]
    """<p>The end time of the time range filter</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TimeRangeFilter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "start_time" in value:
        import aws_sdk_elasticache.types.t_stamp

        aws_sdk_elasticache.types.t_stamp.serialize_query(
            value["start_time"], pairs, f"{prefix}.StartTime"
        )
    if "end_time" in value:
        import aws_sdk_elasticache.types.t_stamp

        aws_sdk_elasticache.types.t_stamp.serialize_query(
            value["end_time"], pairs, f"{prefix}.EndTime"
        )


def deserialize_query(el: Element) -> TimeRangeFilter:
    out: TimeRangeFilter = {}  # type: ignore[typeddict-item]
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import aws_sdk_elasticache.types.t_stamp

        out["start_time"] = aws_sdk_elasticache.types.t_stamp.deserialize_query(
            child_start_time
        )
    child_end_time = el.find("EndTime")
    if child_end_time is not None:
        import aws_sdk_elasticache.types.t_stamp

        out["end_time"] = aws_sdk_elasticache.types.t_stamp.deserialize_query(
            child_end_time
        )
    return out
