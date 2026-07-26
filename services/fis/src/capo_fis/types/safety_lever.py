"""Generated from Smithy shape ``com.amazonaws.fis#SafetyLever``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.resource_arn
    import capo_fis.types.safety_lever_id
    import capo_fis.types.safety_lever_state


class SafetyLever(TypedDict, closed=True):
    id: NotRequired["capo_fis.types.safety_lever_id.SafetyLeverId"]
    """<p> The ID of the safety lever. </p>"""
    arn: NotRequired["capo_fis.types.resource_arn.ResourceArn"]
    """<p> The Amazon Resource Name (ARN) of the safety lever. </p>"""
    state: NotRequired["capo_fis.types.safety_lever_state.SafetyLeverState"]
    """<p> The state of the safety lever. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SafetyLever) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "state" in value:
        import capo_fis.types.safety_lever_state

        out["state"] = capo_fis.types.safety_lever_state.serialize_json(value["state"])
    return out


def deserialize_json(data: dict) -> SafetyLever:
    out: SafetyLever = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "state" in data:
        import capo_fis.types.safety_lever_state

        out["state"] = capo_fis.types.safety_lever_state.deserialize_json(data["state"])
    return out
