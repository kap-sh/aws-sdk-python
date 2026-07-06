"""Generated from Smithy shape ``com.amazonaws.xray#ListRetrievedTracesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_xray.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_xray.types.retrieval_token
    import aws_sdk_xray.types.string
    import aws_sdk_xray.types.trace_format_type


class ListRetrievedTracesRequest(TypedDict, closed=True):
    retrieval_token: "aws_sdk_xray.types.retrieval_token.RetrievalToken"
    """<p> Retrieval token. </p>"""
    trace_format: NotRequired["aws_sdk_xray.types.trace_format_type.TraceFormatType"]
    """<p> Format of the requested traces. </p>"""
    next_token: NotRequired["aws_sdk_xray.types.string.String"]
    """<p> Specify the pagination token returned by a previous request to retrieve the next page of indexes. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRetrievedTracesRequest) -> dict:
    out: dict = {}
    out["RetrievalToken"] = value["retrieval_token"]
    if "trace_format" in value:
        import aws_sdk_xray.types.trace_format_type

        out["TraceFormat"] = aws_sdk_xray.types.trace_format_type.serialize_json(
            value["trace_format"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRetrievedTracesRequest:
    out: ListRetrievedTracesRequest = {}  # type: ignore[typeddict-item]
    if "RetrievalToken" in data:
        out["retrieval_token"] = data["RetrievalToken"]
    else:
        raise DeserializationError(
            "ListRetrievedTracesRequest.retrieval_token required"
        )
    if "TraceFormat" in data:
        import aws_sdk_xray.types.trace_format_type

        out["trace_format"] = aws_sdk_xray.types.trace_format_type.deserialize_json(
            data["TraceFormat"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
