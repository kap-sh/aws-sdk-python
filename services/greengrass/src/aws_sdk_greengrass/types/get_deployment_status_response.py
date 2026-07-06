"""Generated from Smithy shape ``com.amazonaws.greengrass#GetDeploymentStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string
    import aws_sdk_greengrass.types.deployment_type
    import aws_sdk_greengrass.types.error_details


class GetDeploymentStatusResponse(TypedDict, closed=True):
    deployment_status: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The status of the deployment: ''InProgress'', ''Building'', ''Success'', or ''Failure''."""
    deployment_type: NotRequired[
        "aws_sdk_greengrass.types.deployment_type.DeploymentType"
    ]
    """The type of the deployment."""
    error_details: NotRequired["aws_sdk_greengrass.types.error_details.ErrorDetails"]
    """Error details"""
    error_message: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """Error message"""
    updated_at: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The time, in milliseconds since the epoch, when the deployment status was updated."""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeploymentStatusResponse) -> dict:
    out: dict = {}
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
    if "updated_at" in value:
        out["UpdatedAt"] = value["updated_at"]
    return out


def deserialize_json(data: dict) -> GetDeploymentStatusResponse:
    out: GetDeploymentStatusResponse = {}  # type: ignore[typeddict-item]
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
    if "UpdatedAt" in data:
        out["updated_at"] = data["UpdatedAt"]
    return out
