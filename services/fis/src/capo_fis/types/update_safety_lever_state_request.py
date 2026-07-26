"""Generated from Smithy shape ``com.amazonaws.fis#UpdateSafetyLeverStateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_fis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_fis.types.safety_lever_id
    import capo_fis.types.update_safety_lever_state_input


class UpdateSafetyLeverStateRequest(TypedDict, closed=True):
    id: "capo_fis.types.safety_lever_id.SafetyLeverId"
    """<p> The ID of the safety lever. </p>"""
    state: "capo_fis.types.update_safety_lever_state_input.UpdateSafetyLeverStateInput"
    """<p> The state of the safety lever. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSafetyLeverStateRequest) -> dict:
    out: dict = {}
    import capo_fis.types.update_safety_lever_state_input

    out["state"] = capo_fis.types.update_safety_lever_state_input.serialize_json(
        value["state"]
    )
    return out


def deserialize_json(data: dict) -> UpdateSafetyLeverStateRequest:
    out: UpdateSafetyLeverStateRequest = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import capo_fis.types.update_safety_lever_state_input

        out["state"] = capo_fis.types.update_safety_lever_state_input.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("UpdateSafetyLeverStateRequest.state required")
    return out
