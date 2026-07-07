"""Generated from Smithy shape ``com.amazonaws.iot#MitigationAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.mitigation_action_id
    import aws_sdk_iot.types.mitigation_action_name
    import aws_sdk_iot.types.mitigation_action_params
    import aws_sdk_iot.types.role_arn


class MitigationAction(TypedDict, closed=True):
    name: NotRequired["aws_sdk_iot.types.mitigation_action_name.MitigationActionName"]
    """<p>A user-friendly name for the mitigation action.</p>"""
    id: NotRequired["aws_sdk_iot.types.mitigation_action_id.MitigationActionId"]
    """<p>A unique identifier for the mitigation action.</p>"""
    role_arn: NotRequired["aws_sdk_iot.types.role_arn.RoleArn"]
    """<p>The IAM role ARN used to apply this mitigation action.</p>"""
    action_params: NotRequired[
        "aws_sdk_iot.types.mitigation_action_params.MitigationActionParams"
    ]
    """<p>The set of parameters for this mitigation action. The parameters vary, depending on the kind of action you apply.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MitigationAction) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "id" in value:
        out["id"] = value["id"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "action_params" in value:
        import aws_sdk_iot.types.mitigation_action_params

        out["actionParams"] = aws_sdk_iot.types.mitigation_action_params.serialize_json(
            value["action_params"]
        )
    return out


def deserialize_json(data: dict) -> MitigationAction:
    out: MitigationAction = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "id" in data:
        out["id"] = data["id"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "actionParams" in data:
        import aws_sdk_iot.types.mitigation_action_params

        out["action_params"] = (
            aws_sdk_iot.types.mitigation_action_params.deserialize_json(
                data["actionParams"]
            )
        )
    return out
