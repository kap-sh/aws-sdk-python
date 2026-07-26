"""Generated from Smithy shape ``com.amazonaws.ssmsap#PutResourcePermissionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm_sap.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_sap.types.arn
    import capo_ssm_sap.types.permission_action_type


class PutResourcePermissionInput(TypedDict, closed=True):
    action_type: "capo_ssm_sap.types.permission_action_type.PermissionActionType"
    """<p/>"""
    source_resource_arn: "capo_ssm_sap.types.arn.Arn"
    """<p/>"""
    resource_arn: "capo_ssm_sap.types.arn.Arn"
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePermissionInput) -> dict:
    out: dict = {}
    import capo_ssm_sap.types.permission_action_type

    out["ActionType"] = capo_ssm_sap.types.permission_action_type.serialize_json(
        value["action_type"]
    )
    out["SourceResourceArn"] = value["source_resource_arn"]
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> PutResourcePermissionInput:
    out: PutResourcePermissionInput = {}  # type: ignore[typeddict-item]
    if "ActionType" in data:
        import capo_ssm_sap.types.permission_action_type

        out["action_type"] = capo_ssm_sap.types.permission_action_type.deserialize_json(
            data["ActionType"]
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
