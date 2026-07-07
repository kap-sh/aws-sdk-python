"""Generated from Smithy shape ``com.amazonaws.xray#BatchGetTracesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_xray.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_xray.types.string
    import aws_sdk_xray.types.trace_id_list


class BatchGetTracesRequest(TypedDict, closed=True):
    trace_ids: "aws_sdk_xray.types.trace_id_list.TraceIdList"
    """<p>Specify the trace IDs of requests for which to retrieve segments.</p>"""
    next_token: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>Pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetTracesRequest) -> dict:
    out: dict = {}
    import aws_sdk_xray.types.trace_id_list

    out["TraceIds"] = aws_sdk_xray.types.trace_id_list.serialize_json(
        value["trace_ids"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> BatchGetTracesRequest:
    out: BatchGetTracesRequest = {}  # type: ignore[typeddict-item]
    if "TraceIds" in data:
        import aws_sdk_xray.types.trace_id_list

        out["trace_ids"] = aws_sdk_xray.types.trace_id_list.deserialize_json(
            data["TraceIds"]
        )
    else:
        raise DeserializationError("BatchGetTracesRequest.trace_ids required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
