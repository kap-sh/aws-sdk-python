"""Generated from Smithy shape ``com.amazonaws.iot#UpdateMitigationActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.mitigation_action_name
    import capo_iot.types.mitigation_action_params
    import capo_iot.types.role_arn


class UpdateMitigationActionRequest(TypedDict, closed=True):
    action_name: "capo_iot.types.mitigation_action_name.MitigationActionName"
    """<p>The friendly name for the mitigation action. You cannot change the name by using <code>UpdateMitigationAction</code>. Instead, you must delete and recreate the mitigation action with the new name.</p>"""
    role_arn: NotRequired["capo_iot.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM role that is used to apply the mitigation action.</p>"""
    action_params: NotRequired[
        "capo_iot.types.mitigation_action_params.MitigationActionParams"
    ]
    """<p>Defines the type of action and the parameters for that action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMitigationActionRequest) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "action_params" in value:
        import capo_iot.types.mitigation_action_params

        out["actionParams"] = capo_iot.types.mitigation_action_params.serialize_json(
            value["action_params"]
        )
    return out


def deserialize_json(data: dict) -> UpdateMitigationActionRequest:
    out: UpdateMitigationActionRequest = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "actionParams" in data:
        import capo_iot.types.mitigation_action_params

        out["action_params"] = capo_iot.types.mitigation_action_params.deserialize_json(
            data["actionParams"]
        )
    return out
