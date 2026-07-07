"""Generated from Smithy shape ``com.amazonaws.mgn#RemoveTemplateActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.action_id
    import aws_sdk_mgn.types.launch_configuration_template_id


class RemoveTemplateActionRequest(TypedDict, closed=True):
    launch_configuration_template_id: "aws_sdk_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID"
    """<p>Launch configuration template ID of the post migration custom action to remove.</p>"""
    action_id: "aws_sdk_mgn.types.action_id.ActionID"
    """<p>Template post migration custom action ID to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveTemplateActionRequest) -> dict:
    out: dict = {}
    out["launchConfigurationTemplateID"] = value["launch_configuration_template_id"]
    out["actionID"] = value["action_id"]
    return out


def deserialize_json(data: dict) -> RemoveTemplateActionRequest:
    out: RemoveTemplateActionRequest = {}  # type: ignore[typeddict-item]
    if "launchConfigurationTemplateID" in data:
        out["launch_configuration_template_id"] = data["launchConfigurationTemplateID"]
    else:
        raise DeserializationError(
            "RemoveTemplateActionRequest.launch_configuration_template_id required"
        )
    if "actionID" in data:
        out["action_id"] = data["actionID"]
    else:
        raise DeserializationError("RemoveTemplateActionRequest.action_id required")
    return out
