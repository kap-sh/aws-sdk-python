"""Generated from Smithy shape ``com.amazonaws.iot#CreateMitigationActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.mitigation_action_name
    import aws_sdk_iot.types.mitigation_action_params
    import aws_sdk_iot.types.role_arn
    import aws_sdk_iot.types.tag_list


class CreateMitigationActionRequest(TypedDict, closed=True):
    action_name: "aws_sdk_iot.types.mitigation_action_name.MitigationActionName"
    """<p>A friendly name for the action. Choose a friendly name that accurately describes the action (for example, <code>EnableLoggingAction</code>).</p>"""
    role_arn: "aws_sdk_iot.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that is used to apply the mitigation action.</p>"""
    action_params: "aws_sdk_iot.types.mitigation_action_params.MitigationActionParams"
    """<p>Defines the type of action and the parameters for that action.</p>"""
    tags: NotRequired["aws_sdk_iot.types.tag_list.TagList"]
    """<p>Metadata that can be used to manage the mitigation action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMitigationActionRequest) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    import aws_sdk_iot.types.mitigation_action_params

    out["actionParams"] = aws_sdk_iot.types.mitigation_action_params.serialize_json(
        value["action_params"]
    )
    if "tags" in value:
        import aws_sdk_iot.types.tag_list

        out["tags"] = aws_sdk_iot.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateMitigationActionRequest:
    out: CreateMitigationActionRequest = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreateMitigationActionRequest.role_arn required")
    if "actionParams" in data:
        import aws_sdk_iot.types.mitigation_action_params

        out["action_params"] = (
            aws_sdk_iot.types.mitigation_action_params.deserialize_json(
                data["actionParams"]
            )
        )
    else:
        raise DeserializationError(
            "CreateMitigationActionRequest.action_params required"
        )
    if "tags" in data:
        import aws_sdk_iot.types.tag_list

        out["tags"] = aws_sdk_iot.types.tag_list.deserialize_json(data["tags"])
    return out
