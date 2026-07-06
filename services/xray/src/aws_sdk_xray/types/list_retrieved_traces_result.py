"""Generated from Smithy shape ``com.amazonaws.xray#ListRetrievedTracesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_xray.types.retrieval_status
    import aws_sdk_xray.types.string
    import aws_sdk_xray.types.trace_format_type
    import aws_sdk_xray.types.trace_span_list


class ListRetrievedTracesResult(TypedDict, closed=True):
    retrieval_status: NotRequired["aws_sdk_xray.types.retrieval_status.RetrievalStatus"]
    """<p> Status of the retrieval. </p>"""
    trace_format: NotRequired["aws_sdk_xray.types.trace_format_type.TraceFormatType"]
    """<p> Format of the requested traces. </p>"""
    traces: NotRequired["aws_sdk_xray.types.trace_span_list.TraceSpanList"]
    """<p> Full traces for the specified requests. </p>"""
    next_token: NotRequired["aws_sdk_xray.types.string.String"]
    """<p> Specify the pagination token returned by a previous request to retrieve the next page of indexes. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRetrievedTracesResult) -> dict:
    out: dict = {}
    if "retrieval_status" in value:
        import aws_sdk_xray.types.retrieval_status

        out["RetrievalStatus"] = aws_sdk_xray.types.retrieval_status.serialize_json(
            value["retrieval_status"]
        )
    if "trace_format" in value:
        import aws_sdk_xray.types.trace_format_type

        out["TraceFormat"] = aws_sdk_xray.types.trace_format_type.serialize_json(
            value["trace_format"]
        )
    if "traces" in value:
        import aws_sdk_xray.types.trace_span_list

        out["Traces"] = aws_sdk_xray.types.trace_span_list.serialize_json(
            value["traces"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRetrievedTracesResult:
    out: ListRetrievedTracesResult = {}  # type: ignore[typeddict-item]
    if "RetrievalStatus" in data:
        import aws_sdk_xray.types.retrieval_status

        out["retrieval_status"] = aws_sdk_xray.types.retrieval_status.deserialize_json(
            data["RetrievalStatus"]
        )
    if "TraceFormat" in data:
        import aws_sdk_xray.types.trace_format_type

        out["trace_format"] = aws_sdk_xray.types.trace_format_type.deserialize_json(
            data["TraceFormat"]
        )
    if "Traces" in data:
        import aws_sdk_xray.types.trace_span_list

        out["traces"] = aws_sdk_xray.types.trace_span_list.deserialize_json(
            data["Traces"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
