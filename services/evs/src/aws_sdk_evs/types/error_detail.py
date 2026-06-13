"""Generated from Smithy shape ``com.amazonaws.evs#ErrorDetail``."""

from typing import TypedDict

from aws_sdk_evs.errors import DeserializationError


class ErrorDetail(TypedDict):
    error_code: "str"
    """<p>The error code.</p>"""
    error_message: "str"
    """<p>The error message.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ErrorDetail) -> dict:
    out: dict = {}
    out["errorCode"] = value["error_code"]
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ErrorDetail:
    out: ErrorDetail = {}  # type: ignore[typeddict-item]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    else:
        raise DeserializationError("ErrorDetail.error_code required")
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    else:
        raise DeserializationError("ErrorDetail.error_message required")
    return out
