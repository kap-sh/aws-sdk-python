"""Generated from Smithy shape ``com.amazonaws.fis#UpdateSafetyLeverStateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_fis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fis.types.safety_lever_status_input
    import aws_sdk_fis.types.safety_lever_status_reason


class UpdateSafetyLeverStateInput(TypedDict, closed=True):
    status: "aws_sdk_fis.types.safety_lever_status_input.SafetyLeverStatusInput"
    """<p> The updated state of the safety lever. </p>"""
    reason: "aws_sdk_fis.types.safety_lever_status_reason.SafetyLeverStatusReason"
    """<p> The reason for updating the state of the safety lever. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSafetyLeverStateInput) -> dict:
    out: dict = {}
    import aws_sdk_fis.types.safety_lever_status_input

    out["status"] = aws_sdk_fis.types.safety_lever_status_input.serialize_json(
        value["status"]
    )
    out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> UpdateSafetyLeverStateInput:
    out: UpdateSafetyLeverStateInput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_fis.types.safety_lever_status_input

        out["status"] = aws_sdk_fis.types.safety_lever_status_input.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("UpdateSafetyLeverStateInput.status required")
    if "reason" in data:
        out["reason"] = data["reason"]
    else:
        raise DeserializationError("UpdateSafetyLeverStateInput.reason required")
    return out
