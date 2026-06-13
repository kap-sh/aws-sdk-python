"""Generated from Smithy shape ``com.amazonaws.ssmsap#PutResourcePermissionInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm_sap.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.arn
    import aws_sdk_ssm_sap.types.permission_action_type


class PutResourcePermissionInput(TypedDict):
    action_type: "aws_sdk_ssm_sap.types.permission_action_type.PermissionActionType"
    """<p/>"""
    source_resource_arn: "aws_sdk_ssm_sap.types.arn.Arn"
    """<p/>"""
    resource_arn: "aws_sdk_ssm_sap.types.arn.Arn"
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePermissionInput) -> dict:
    out: dict = {}
    import aws_sdk_ssm_sap.types.permission_action_type

    out["ActionType"] = aws_sdk_ssm_sap.types.permission_action_type.serialize_json(
        value["action_type"]
    )
    out["SourceResourceArn"] = value["source_resource_arn"]
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> PutResourcePermissionInput:
    out: PutResourcePermissionInput = {}  # type: ignore[typeddict-item]
    if "ActionType" in data:
        import aws_sdk_ssm_sap.types.permission_action_type

        out["action_type"] = (
            aws_sdk_ssm_sap.types.permission_action_type.deserialize_json(
                data["ActionType"]
            )
        )
    else:
        raise DeserializationError("PutResourcePermissionInput.action_type required")
    if "SourceResourceArn" in data:
        out["source_resource_arn"] = data["SourceResourceArn"]
    else:
        raise DeserializationError(
            "PutResourcePermissionInput.source_resource_arn required"
        )
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("PutResourcePermissionInput.resource_arn required")
    return out
