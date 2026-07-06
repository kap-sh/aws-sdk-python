"""Generated from Smithy shape ``com.amazonaws.xray#BatchGetTracesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_xray.types.string
    import aws_sdk_xray.types.trace_list
    import aws_sdk_xray.types.unprocessed_trace_id_list


class BatchGetTracesResult(TypedDict, closed=True):
    traces: NotRequired["aws_sdk_xray.types.trace_list.TraceList"]
    """<p>Full traces for the specified requests.</p>"""
    unprocessed_trace_ids: NotRequired[
        "aws_sdk_xray.types.unprocessed_trace_id_list.UnprocessedTraceIdList"
    ]
    """<p>Trace IDs of requests that haven't been processed.</p>"""
    next_token: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>Pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetTracesResult) -> dict:
    out: dict = {}
    if "traces" in value:
        import aws_sdk_xray.types.trace_list

        out["Traces"] = aws_sdk_xray.types.trace_list.serialize_json(value["traces"])
    if "unprocessed_trace_ids" in value:
        import aws_sdk_xray.types.unprocessed_trace_id_list

        out["UnprocessedTraceIds"] = (
            aws_sdk_xray.types.unprocessed_trace_id_list.serialize_json(
                value["unprocessed_trace_ids"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> BatchGetTracesResult:
    out: BatchGetTracesResult = {}  # type: ignore[typeddict-item]
    if "Traces" in data:
        import aws_sdk_xray.types.trace_list

        out["traces"] = aws_sdk_xray.types.trace_list.deserialize_json(data["Traces"])
    if "UnprocessedTraceIds" in data:
        import aws_sdk_xray.types.unprocessed_trace_id_list

        out["unprocessed_trace_ids"] = (
            aws_sdk_xray.types.unprocessed_trace_id_list.deserialize_json(
                data["UnprocessedTraceIds"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
