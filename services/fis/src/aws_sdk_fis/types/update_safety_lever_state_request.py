"""Generated from Smithy shape ``com.amazonaws.fis#UpdateSafetyLeverStateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_fis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fis.types.safety_lever_id
    import aws_sdk_fis.types.update_safety_lever_state_input


class UpdateSafetyLeverStateRequest(TypedDict):
    id: "aws_sdk_fis.types.safety_lever_id.SafetyLeverId"
    """<p> The ID of the safety lever. </p>"""
    state: (
        "aws_sdk_fis.types.update_safety_lever_state_input.UpdateSafetyLeverStateInput"
    )
    """<p> The state of the safety lever. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSafetyLeverStateRequest) -> dict:
    out: dict = {}
    import aws_sdk_fis.types.update_safety_lever_state_input

    out["state"] = aws_sdk_fis.types.update_safety_lever_state_input.serialize_json(
        value["state"]
    )
    return out


def deserialize_json(data: dict) -> UpdateSafetyLeverStateRequest:
    out: UpdateSafetyLeverStateRequest = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import aws_sdk_fis.types.update_safety_lever_state_input

        out["state"] = (
            aws_sdk_fis.types.update_safety_lever_state_input.deserialize_json(
                data["state"]
            )
        )
    else:
        raise DeserializationError("UpdateSafetyLeverStateRequest.state required")
    return out
