"""Generated from Smithy shape ``com.amazonaws.tnb#ErrorInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_tnb.types.error_cause
    import aws_sdk_tnb.types.error_details


class ErrorInfo(TypedDict, closed=True):
    cause: NotRequired["aws_sdk_tnb.types.error_cause.ErrorCause"]
    """<p>Error cause.</p>"""
    details: NotRequired["aws_sdk_tnb.types.error_details.ErrorDetails"]
    """<p>Error details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorInfo) -> dict:
    out: dict = {}
    if "cause" in value:
        out["cause"] = value["cause"]
    if "details" in value:
        out["details"] = value["details"]
    return out


def deserialize_json(data: dict) -> ErrorInfo:
    out: ErrorInfo = {}  # type: ignore[typeddict-item]
    if "cause" in data:
        out["cause"] = data["cause"]
    if "details" in data:
        out["details"] = data["details"]
    return out
