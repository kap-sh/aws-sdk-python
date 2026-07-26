"""Generated from Smithy shape ``com.amazonaws.iot#UpdateMitigationActionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.mitigation_action_arn
    import capo_iot.types.mitigation_action_id


class UpdateMitigationActionResponse(TypedDict, closed=True):
    action_arn: NotRequired["capo_iot.types.mitigation_action_arn.MitigationActionArn"]
    """<p>The ARN for the new mitigation action.</p>"""
    action_id: NotRequired["capo_iot.types.mitigation_action_id.MitigationActionId"]
    """<p>A unique identifier for the mitigation action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMitigationActionResponse) -> dict:
    out: dict = {}
    if "action_arn" in value:
        out["actionArn"] = value["action_arn"]
    if "action_id" in value:
        out["actionId"] = value["action_id"]
    return out


def deserialize_json(data: dict) -> UpdateMitigationActionResponse:
    out: UpdateMitigationActionResponse = {}  # type: ignore[typeddict-item]
    if "actionArn" in data:
        out["action_arn"] = data["actionArn"]
    if "actionId" in data:
        out["action_id"] = data["actionId"]
    return out
