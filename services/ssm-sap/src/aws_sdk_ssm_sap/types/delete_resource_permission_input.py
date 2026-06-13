"""Generated from Smithy shape ``com.amazonaws.ssmsap#DeleteResourcePermissionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_sap.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.arn
    import aws_sdk_ssm_sap.types.permission_action_type


class DeleteResourcePermissionInput(TypedDict):
    action_type: NotRequired[
        "aws_sdk_ssm_sap.types.permission_action_type.PermissionActionType"
    ]
    """<p>Delete or restore the permissions on the target database.</p>"""
    source_resource_arn: NotRequired["aws_sdk_ssm_sap.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the source resource.</p>"""
    resource_arn: "aws_sdk_ssm_sap.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourcePermissionInput) -> dict:
    out: dict = {}
    if "action_type" in value:
        import aws_sdk_ssm_sap.types.permission_action_type

        out["ActionType"] = aws_sdk_ssm_sap.types.permission_action_type.serialize_json(
            value["action_type"]
        )
    if "source_resource_arn" in value:
        out["SourceResourceArn"] = value["source_resource_arn"]
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> DeleteResourcePermissionInput:
    out: DeleteResourcePermissionInput = {}  # type: ignore[typeddict-item]
    if "ActionType" in data:
        import aws_sdk_ssm_sap.types.permission_action_type

        out["action_type"] = (
            aws_sdk_ssm_sap.types.permission_action_type.deserialize_json(
                data["ActionType"]
            )
        )
    if "SourceResourceArn" in data:
        out["source_resource_arn"] = data["SourceResourceArn"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError(
            "DeleteResourcePermissionInput.resource_arn required"
        )
    return out
