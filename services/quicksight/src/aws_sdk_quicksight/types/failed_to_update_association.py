"""Generated from Smithy shape ``com.amazonaws.quicksight#FailedToUpdateAssociation``."""

from typing import TypedDict

from typing_extensions import NotRequired


class FailedToUpdateAssociation(TypedDict):
    arn: NotRequired["str"]
    """<p>The ARN that could not be added or removed.</p>"""
    error_message: NotRequired["str"]
    """<p>A description of the failure.</p>"""
    error_code: NotRequired["str"]
    """<p>The error code for the failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailedToUpdateAssociation) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    return out


def deserialize_json(data: dict) -> FailedToUpdateAssociation:
    out: FailedToUpdateAssociation = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    return out
