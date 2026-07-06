"""Generated from Smithy shape ``com.amazonaws.fis#SafetyLeverState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.safety_lever_status
    import aws_sdk_fis.types.safety_lever_status_reason


class SafetyLeverState(TypedDict, closed=True):
    status: NotRequired["aws_sdk_fis.types.safety_lever_status.SafetyLeverStatus"]
    """<p> The state of the safety lever. </p>"""
    reason: NotRequired[
        "aws_sdk_fis.types.safety_lever_status_reason.SafetyLeverStatusReason"
    ]
    """<p> The reason for the state of the safety lever. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SafetyLeverState) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_fis.types.safety_lever_status

        out["status"] = aws_sdk_fis.types.safety_lever_status.serialize_json(
            value["status"]
        )
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> SafetyLeverState:
    out: SafetyLeverState = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_fis.types.safety_lever_status

        out["status"] = aws_sdk_fis.types.safety_lever_status.deserialize_json(
            data["status"]
        )
    if "reason" in data:
        out["reason"] = data["reason"]
    return out
