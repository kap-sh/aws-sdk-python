"""Generated from Smithy shape ``com.amazonaws.dax#DescribeEventsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dax.types.integer_optional
    import aws_sdk_dax.types.source_type
    import aws_sdk_dax.types.string
    import aws_sdk_dax.types.t_stamp


class DescribeEventsRequest(TypedDict):
    source_name: NotRequired["aws_sdk_dax.types.string.String"]
    """<p>The identifier of the event source for which events will be returned. If not specified, then all sources are included in the response.</p>"""
    source_type: NotRequired["aws_sdk_dax.types.source_type.SourceType"]
    """<p>The event source to retrieve events for. If no value is specified, all events are returned.</p>"""
    start_time: NotRequired["aws_sdk_dax.types.t_stamp.TStamp"]
    """<p>The beginning of the time interval to retrieve events for, specified in ISO 8601 format.</p>"""
    end_time: NotRequired["aws_sdk_dax.types.t_stamp.TStamp"]
    """<p>The end of the time interval for which to retrieve events, specified in ISO 8601 format.</p>"""
    duration: NotRequired["aws_sdk_dax.types.integer_optional.IntegerOptional"]
    """<p>The number of minutes' worth of events to retrieve.</p>"""
    max_results: NotRequired["aws_sdk_dax.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p> <p>The value for <code>MaxResults</code> must be between 20 and 100.</p>"""
    next_token: NotRequired["aws_sdk_dax.types.string.String"]
    """<p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by <code>MaxResults</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventsRequest) -> dict:
    out: dict = {}
    if "source_name" in value:
        out["SourceName"] = value["source_name"]
    if "source_type" in value:
        import aws_sdk_dax.types.source_type

        out["SourceType"] = aws_sdk_dax.types.source_type.serialize_aws_json_1_1(
            value["source_type"]
        )
    if "start_time" in value:
        import aws_sdk_dax.types.t_stamp

        out["StartTime"] = aws_sdk_dax.types.t_stamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_dax.types.t_stamp

        out["EndTime"] = aws_sdk_dax.types.t_stamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "duration" in value:
        out["Duration"] = value["duration"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventsRequest:
    out: DescribeEventsRequest = {}  # type: ignore[typeddict-item]
    if "SourceName" in data:
        out["source_name"] = data["SourceName"]
    if "SourceType" in data:
        import aws_sdk_dax.types.source_type

        out["source_type"] = aws_sdk_dax.types.source_type.deserialize_aws_json_1_1(
            data["SourceType"]
        )
    if "StartTime" in data:
        import aws_sdk_dax.types.t_stamp

        out["start_time"] = aws_sdk_dax.types.t_stamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_dax.types.t_stamp

        out["end_time"] = aws_sdk_dax.types.t_stamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "Duration" in data:
        out["duration"] = data["Duration"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
