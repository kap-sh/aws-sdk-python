"""Generated from Smithy shape ``com.amazonaws.xray#GetTraceSummariesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_xray.types.nullable_long
    import aws_sdk_xray.types.string
    import aws_sdk_xray.types.timestamp
    import aws_sdk_xray.types.trace_summary_list


class GetTraceSummariesResult(TypedDict):
    trace_summaries: NotRequired[
        "aws_sdk_xray.types.trace_summary_list.TraceSummaryList"
    ]
    """<p>Trace IDs and annotations for traces that were found in the specified time frame.</p>"""
    approximate_time: NotRequired["aws_sdk_xray.types.timestamp.Timestamp"]
    """<p>The start time of this page of results.</p>"""
    traces_processed_count: NotRequired["aws_sdk_xray.types.nullable_long.NullableLong"]
    """<p>The total number of traces processed, including traces that did not match the specified filter expression.</p>"""
    next_token: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>If the requested time frame contained more than one page of results, you can use this token to retrieve the next page. The first page contains the most recent results, closest to the end of the time frame.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTraceSummariesResult) -> dict:
    out: dict = {}
    if "trace_summaries" in value:
        import aws_sdk_xray.types.trace_summary_list

        out["TraceSummaries"] = aws_sdk_xray.types.trace_summary_list.serialize_json(
            value["trace_summaries"]
        )
    if "approximate_time" in value:
        import aws_sdk_xray.types.timestamp

        out["ApproximateTime"] = aws_sdk_xray.types.timestamp.serialize_json(
            value["approximate_time"]
        )
    if "traces_processed_count" in value:
        out["TracesProcessedCount"] = value["traces_processed_count"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetTraceSummariesResult:
    out: GetTraceSummariesResult = {}  # type: ignore[typeddict-item]
    if "TraceSummaries" in data:
        import aws_sdk_xray.types.trace_summary_list

        out["trace_summaries"] = aws_sdk_xray.types.trace_summary_list.deserialize_json(
            data["TraceSummaries"]
        )
    if "ApproximateTime" in data:
        import aws_sdk_xray.types.timestamp

        out["approximate_time"] = aws_sdk_xray.types.timestamp.deserialize_json(
            data["ApproximateTime"]
        )
    if "TracesProcessedCount" in data:
        out["traces_processed_count"] = data["TracesProcessedCount"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
