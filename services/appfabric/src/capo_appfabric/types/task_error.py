"""Generated from Smithy shape ``com.amazonaws.appfabric#TaskError``."""

from typing_extensions import NotRequired, TypedDict


class TaskError(TypedDict, closed=True):
    error_code: NotRequired["str"]
    """<p>The code of the error.</p>"""
    error_message: NotRequired["str"]
    """<p>The message of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaskError) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> TaskError:
    out: TaskError = {}  # type: ignore[typeddict-item]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
