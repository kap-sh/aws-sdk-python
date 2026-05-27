"""Generated from Smithy shape ``com.amazonaws.lambda#InvokeWithResponseStreamCompleteEvent``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.string


class InvokeWithResponseStreamCompleteEvent(TypedDict):
    error_code: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>An error code.</p>"""
    error_details: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The details of any returned error.</p>"""
    log_result: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The last 4 KB of the execution log, which is base64-encoded.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeWithResponseStreamCompleteEvent) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_details" in value:
        out["ErrorDetails"] = value["error_details"]
    if "log_result" in value:
        out["LogResult"] = value["log_result"]
    return out


def deserialize_json(data: dict) -> InvokeWithResponseStreamCompleteEvent:
    out: InvokeWithResponseStreamCompleteEvent = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorDetails" in data:
        out["error_details"] = data["ErrorDetails"]
    if "LogResult" in data:
        out["log_result"] = data["LogResult"]
    return out
