"""Generated from Smithy shape ``com.amazonaws.iot#StatusReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.status_reason_code
    import capo_iot.types.status_reason_description


class StatusReason(TypedDict, closed=True):
    reason_code: "capo_iot.types.status_reason_code.StatusReasonCode"
    """<p>A code that provides additional context for the command execution status.</p>"""
    reason_description: NotRequired[
        "capo_iot.types.status_reason_description.StatusReasonDescription"
    ]
    """<p>A literal string for devices to optionally provide additional information about the reason code for a command execution status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StatusReason) -> dict:
    out: dict = {}
    out["reasonCode"] = value["reason_code"]
    if "reason_description" in value:
        out["reasonDescription"] = value["reason_description"]
    return out


def deserialize_json(data: dict) -> StatusReason:
    out: StatusReason = {}  # type: ignore[typeddict-item]
    if "reasonCode" in data:
        out["reason_code"] = data["reasonCode"]
    else:
        raise DeserializationError("StatusReason.reason_code required")
    if "reasonDescription" in data:
        out["reason_description"] = data["reasonDescription"]
    return out
