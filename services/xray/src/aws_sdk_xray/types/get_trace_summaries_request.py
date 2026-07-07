"""Generated from Smithy shape ``com.amazonaws.xray#GetTraceSummariesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_xray.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_xray.types.filter_expression
    import aws_sdk_xray.types.nullable_boolean
    import aws_sdk_xray.types.sampling_strategy
    import aws_sdk_xray.types.string
    import aws_sdk_xray.types.time_range_type
    import aws_sdk_xray.types.timestamp


class GetTraceSummariesRequest(TypedDict, closed=True):
    start_time: "aws_sdk_xray.types.timestamp.Timestamp"
    """<p>The start of the time frame for which to retrieve traces.</p>"""
    end_time: "aws_sdk_xray.types.timestamp.Timestamp"
    """<p>The end of the time frame for which to retrieve traces.</p>"""
    time_range_type: NotRequired["aws_sdk_xray.types.time_range_type.TimeRangeType"]
    """<p>Query trace summaries by TraceId (trace start time), Event (trace update time), or Service (trace segment end time).</p>"""
    sampling: NotRequired["aws_sdk_xray.types.nullable_boolean.NullableBoolean"]
    """<p>Set to <code>true</code> to get summaries for only a subset of available traces.</p>"""
    sampling_strategy: NotRequired[
        "aws_sdk_xray.types.sampling_strategy.SamplingStrategy"
    ]
    """<p>A parameter to indicate whether to enable sampling on trace summaries. Input parameters are Name and Value.</p>"""
    filter_expression: NotRequired[
        "aws_sdk_xray.types.filter_expression.FilterExpression"
    ]
    """<p>Specify a filter expression to retrieve trace summaries for services or requests that meet certain requirements.</p>"""
    next_token: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>Specify the pagination token returned by a previous request to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTraceSummariesRequest) -> dict:
    out: dict = {}
    import aws_sdk_xray.types.timestamp

    out["StartTime"] = aws_sdk_xray.types.timestamp.serialize_json(value["start_time"])
    import aws_sdk_xray.types.timestamp

    out["EndTime"] = aws_sdk_xray.types.timestamp.serialize_json(value["end_time"])
    if "time_range_type" in value:
        import aws_sdk_xray.types.time_range_type

        out["TimeRangeType"] = aws_sdk_xray.types.time_range_type.serialize_json(
            value["time_range_type"]
        )
    if "sampling" in value:
        out["Sampling"] = value["sampling"]
    if "sampling_strategy" in value:
        import aws_sdk_xray.types.sampling_strategy

        out["SamplingStrategy"] = aws_sdk_xray.types.sampling_strategy.serialize_json(
            value["sampling_strategy"]
        )
    if "filter_expression" in value:
        out["FilterExpression"] = value["filter_expression"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetTraceSummariesRequest:
    out: GetTraceSummariesRequest = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import aws_sdk_xray.types.timestamp

        out["start_time"] = aws_sdk_xray.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    else:
        raise DeserializationError("GetTraceSummariesRequest.start_time required")
    if "EndTime" in data:
        import aws_sdk_xray.types.timestamp

        out["end_time"] = aws_sdk_xray.types.timestamp.deserialize_json(data["EndTime"])
    else:
        raise DeserializationError("GetTraceSummariesRequest.end_time required")
    if "TimeRangeType" in data:
        import aws_sdk_xray.types.time_range_type

        out["time_range_type"] = aws_sdk_xray.types.time_range_type.deserialize_json(
            data["TimeRangeType"]
        )
    if "Sampling" in data:
        out["sampling"] = data["Sampling"]
    if "SamplingStrategy" in data:
        import aws_sdk_xray.types.sampling_strategy

        out["sampling_strategy"] = (
            aws_sdk_xray.types.sampling_strategy.deserialize_json(
                data["SamplingStrategy"]
            )
        )
    if "FilterExpression" in data:
        out["filter_expression"] = data["FilterExpression"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
