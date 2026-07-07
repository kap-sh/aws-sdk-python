"""Generated from Smithy shape ``com.amazonaws.iot#DescribeMitigationActionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.mitigation_action_arn
    import aws_sdk_iot.types.mitigation_action_id
    import aws_sdk_iot.types.mitigation_action_name
    import aws_sdk_iot.types.mitigation_action_params
    import aws_sdk_iot.types.mitigation_action_type
    import aws_sdk_iot.types.role_arn
    import aws_sdk_iot.types.timestamp


class DescribeMitigationActionResponse(TypedDict, closed=True):
    action_name: NotRequired[
        "aws_sdk_iot.types.mitigation_action_name.MitigationActionName"
    ]
    """<p>The friendly name that uniquely identifies the mitigation action.</p>"""
    action_type: NotRequired[
        "aws_sdk_iot.types.mitigation_action_type.MitigationActionType"
    ]
    """<p>The type of mitigation action.</p>"""
    action_arn: NotRequired[
        "aws_sdk_iot.types.mitigation_action_arn.MitigationActionArn"
    ]
    """<p>The ARN that identifies this migration action.</p>"""
    action_id: NotRequired["aws_sdk_iot.types.mitigation_action_id.MitigationActionId"]
    """<p>A unique identifier for this action.</p>"""
    role_arn: NotRequired["aws_sdk_iot.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM role used to apply this action.</p>"""
    action_params: NotRequired[
        "aws_sdk_iot.types.mitigation_action_params.MitigationActionParams"
    ]
    """<p>Parameters that control how the mitigation action is applied, specific to the type of mitigation action.</p>"""
    creation_date: NotRequired["aws_sdk_iot.types.timestamp.Timestamp"]
    """<p>The date and time when the mitigation action was added to your Amazon Web Services accounts.</p>"""
    last_modified_date: NotRequired["aws_sdk_iot.types.timestamp.Timestamp"]
    """<p>The date and time when the mitigation action was last changed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeMitigationActionResponse) -> dict:
    out: dict = {}
    if "action_name" in value:
        out["actionName"] = value["action_name"]
    if "action_type" in value:
        import aws_sdk_iot.types.mitigation_action_type

        out["actionType"] = aws_sdk_iot.types.mitigation_action_type.serialize_json(
            value["action_type"]
        )
    if "action_arn" in value:
        out["actionArn"] = value["action_arn"]
    if "action_id" in value:
        out["actionId"] = value["action_id"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "action_params" in value:
        import aws_sdk_iot.types.mitigation_action_params

        out["actionParams"] = aws_sdk_iot.types.mitigation_action_params.serialize_json(
            value["action_params"]
        )
    if "creation_date" in value:
        import aws_sdk_iot.types.timestamp

        out["creationDate"] = aws_sdk_iot.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "last_modified_date" in value:
        import aws_sdk_iot.types.timestamp

        out["lastModifiedDate"] = aws_sdk_iot.types.timestamp.serialize_json(
            value["last_modified_date"]
        )
    return out


def deserialize_json(data: dict) -> DescribeMitigationActionResponse:
    out: DescribeMitigationActionResponse = {}  # type: ignore[typeddict-item]
    if "actionName" in data:
        out["action_name"] = data["actionName"]
    if "actionType" in data:
        import aws_sdk_iot.types.mitigation_action_type

        out["action_type"] = aws_sdk_iot.types.mitigation_action_type.deserialize_json(
            data["actionType"]
        )
    if "actionArn" in data:
        out["action_arn"] = data["actionArn"]
    if "actionId" in data:
        out["action_id"] = data["actionId"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "actionParams" in data:
        import aws_sdk_iot.types.mitigation_action_params

        out["action_params"] = (
            aws_sdk_iot.types.mitigation_action_params.deserialize_json(
                data["actionParams"]
            )
        )
    if "creationDate" in data:
        import aws_sdk_iot.types.timestamp

        out["creation_date"] = aws_sdk_iot.types.timestamp.deserialize_json(
            data["creationDate"]
        )
    if "lastModifiedDate" in data:
        import aws_sdk_iot.types.timestamp

        out["last_modified_date"] = aws_sdk_iot.types.timestamp.deserialize_json(
            data["lastModifiedDate"]
        )
    return out
