"""Generated from Smithy shape ``com.amazonaws.pcs#ErrorInfo``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ErrorInfo(TypedDict):
    code: NotRequired["str"]
    """<p>The short-form error code.</p>"""
    message: NotRequired["str"]
    """<p>The detailed error information.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ErrorInfo) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ErrorInfo:
    out: ErrorInfo = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    if "message" in data:
        out["message"] = data["message"]
    return out
