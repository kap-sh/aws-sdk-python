"""Generated from Smithy shape ``com.amazonaws.kafka#ErrorInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class ErrorInfo(TypedDict):
    error_code: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>A number describing the error programmatically.</p>"""
    error_string: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>An optional field to provide more details about the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorInfo) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "error_string" in value:
        out["errorString"] = value["error_string"]
    return out


def deserialize_json(data: dict) -> ErrorInfo:
    out: ErrorInfo = {}  # type: ignore[typeddict-item]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    if "errorString" in data:
        out["error_string"] = data["errorString"]
    return out
