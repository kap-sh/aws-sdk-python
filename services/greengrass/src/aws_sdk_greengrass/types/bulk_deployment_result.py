"""Generated from Smithy shape ``com.amazonaws.greengrass#BulkDeploymentResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string
    import aws_sdk_greengrass.types.deployment_type
    import aws_sdk_greengrass.types.error_details


class BulkDeploymentResult(TypedDict, closed=True):
    created_at: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The time, in ISO format, when the deployment was created."""
    deployment_arn: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ARN of the group deployment."""
    deployment_id: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ID of the group deployment."""
    deployment_status: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The current status of the group deployment: ''InProgress'', ''Building'', ''Success'', or ''Failure''."""
    deployment_type: NotRequired[
        "aws_sdk_greengrass.types.deployment_type.DeploymentType"
    ]
    """The type of the deployment."""
    error_details: NotRequired["aws_sdk_greengrass.types.error_details.ErrorDetails"]
    """Details about the error."""
    error_message: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The error message for a failed deployment"""
    group_arn: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ARN of the Greengrass group."""


# --- restJson1 ser/de ---
def serialize_json(value: BulkDeploymentResult) -> dict:
    out: dict = {}
    if "created_at" in value:
        out["CreatedAt"] = value["created_at"]
    if "deployment_arn" in value:
        out["DeploymentArn"] = value["deployment_arn"]
    if "deployment_id" in value:
        out["DeploymentId"] = value["deployment_id"]
    if "deployment_status" in value:
        out["DeploymentStatus"] = value["deployment_status"]
    if "deployment_type" in value:
        import aws_sdk_greengrass.types.deployment_type

        out["DeploymentType"] = aws_sdk_greengrass.types.deployment_type.serialize_json(
            value["deployment_type"]
        )
    if "error_details" in value:
        import aws_sdk_greengrass.types.error_details

        out["ErrorDetails"] = aws_sdk_greengrass.types.error_details.serialize_json(
            value["error_details"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "group_arn" in value:
        out["GroupArn"] = value["group_arn"]
    return out


def deserialize_json(data: dict) -> BulkDeploymentResult:
    out: BulkDeploymentResult = {}  # type: ignore[typeddict-item]
    if "CreatedAt" in data:
        out["created_at"] = data["CreatedAt"]
    if "DeploymentArn" in data:
        out["deployment_arn"] = data["DeploymentArn"]
    if "DeploymentId" in data:
        out["deployment_id"] = data["DeploymentId"]
    if "DeploymentStatus" in data:
        out["deployment_status"] = data["DeploymentStatus"]
    if "DeploymentType" in data:
        import aws_sdk_greengrass.types.deployment_type

        out["deployment_type"] = (
            aws_sdk_greengrass.types.deployment_type.deserialize_json(
                data["DeploymentType"]
            )
        )
    if "ErrorDetails" in data:
        import aws_sdk_greengrass.types.error_details

        out["error_details"] = aws_sdk_greengrass.types.error_details.deserialize_json(
            data["ErrorDetails"]
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "GroupArn" in data:
        out["group_arn"] = data["GroupArn"]
    return out
