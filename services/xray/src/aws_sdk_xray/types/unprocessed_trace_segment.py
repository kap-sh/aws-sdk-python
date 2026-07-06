"""Generated from Smithy shape ``com.amazonaws.xray#UnprocessedTraceSegment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_xray.types.string


class UnprocessedTraceSegment(TypedDict, closed=True):
    id: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>The segment's ID.</p>"""
    error_code: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>The error that caused processing to fail.</p>"""
    message: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedTraceSegment) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnprocessedTraceSegment:
    out: UnprocessedTraceSegment = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
