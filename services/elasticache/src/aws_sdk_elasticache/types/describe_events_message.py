"""Generated from Smithy shape ``com.amazonaws.elasticache#DescribeEventsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.integer_optional
    import aws_sdk_elasticache.types.source_type
    import aws_sdk_elasticache.types.string
    import aws_sdk_elasticache.types.t_stamp


class DescribeEventsMessage(TypedDict, closed=True):
    source_identifier: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The identifier of the event source for which events are returned. If not specified, all sources are included in the response.</p>"""
    source_type: NotRequired["aws_sdk_elasticache.types.source_type.SourceType"]
    """<p>The event source to retrieve events for. If no value is specified, all events are returned.</p>"""
    start_time: NotRequired["aws_sdk_elasticache.types.t_stamp.TStamp"]
    """<p>The beginning of the time interval to retrieve events for, specified in ISO 8601 format.</p> <p> <b>Example:</b> 2017-03-30T07:03:49.555Z</p>"""
    end_time: NotRequired["aws_sdk_elasticache.types.t_stamp.TStamp"]
    """<p>The end of the time interval for which to retrieve events, specified in ISO 8601 format.</p> <p> <b>Example:</b> 2017-03-30T07:03:49.555Z</p>"""
    duration: NotRequired["aws_sdk_elasticache.types.integer_optional.IntegerOptional"]
    """<p>The number of minutes worth of events to retrieve.</p>"""
    max_records: NotRequired[
        "aws_sdk_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: minimum 20; maximum 100.</p>"""
    marker: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeEventsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "source_identifier" in value:
        pairs.append((f"{prefix}.SourceIdentifier", str(value["source_identifier"])))
    if "source_type" in value:
        import aws_sdk_elasticache.types.source_type

        aws_sdk_elasticache.types.source_type.serialize_query(
            value["source_type"], pairs, f"{prefix}.SourceType"
        )
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
    if "duration" in value:
        pairs.append((f"{prefix}.Duration", str(value["duration"])))
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeEventsMessage:
    out: DescribeEventsMessage = {}  # type: ignore[typeddict-item]
    child_source_identifier = el.find("SourceIdentifier")
    if child_source_identifier is not None:
        out["source_identifier"] = str(child_source_identifier.text or "")
    child_source_type = el.find("SourceType")
    if child_source_type is not None:
        import aws_sdk_elasticache.types.source_type

        out["source_type"] = aws_sdk_elasticache.types.source_type.deserialize_query(
            child_source_type
        )
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
    child_duration = el.find("Duration")
    if child_duration is not None:
        out["duration"] = int(child_duration.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
