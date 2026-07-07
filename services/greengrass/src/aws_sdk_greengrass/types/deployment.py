"""Generated from Smithy shape ``com.amazonaws.greengrass#Deployment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string
    import aws_sdk_greengrass.types.deployment_type


class Deployment(TypedDict, closed=True):
    created_at: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The time, in milliseconds since the epoch, when the deployment was created."""
    deployment_arn: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ARN of the deployment."""
    deployment_id: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ID of the deployment."""
    deployment_type: NotRequired[
        "aws_sdk_greengrass.types.deployment_type.DeploymentType"
    ]
    """The type of the deployment."""
    group_arn: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ARN of the group for this deployment."""


# --- restJson1 ser/de ---
def serialize_json(value: Deployment) -> dict:
    out: dict = {}
    if "created_at" in value:
        out["CreatedAt"] = value["created_at"]
    if "deployment_arn" in value:
        out["DeploymentArn"] = value["deployment_arn"]
    if "deployment_id" in value:
        out["DeploymentId"] = value["deployment_id"]
    if "deployment_type" in value:
        import aws_sdk_greengrass.types.deployment_type

        out["DeploymentType"] = aws_sdk_greengrass.types.deployment_type.serialize_json(
            value["deployment_type"]
        )
    if "group_arn" in value:
        out["GroupArn"] = value["group_arn"]
    return out


def deserialize_json(data: dict) -> Deployment:
    out: Deployment = {}  # type: ignore[typeddict-item]
    if "CreatedAt" in data:
        out["created_at"] = data["CreatedAt"]
    if "DeploymentArn" in data:
        out["deployment_arn"] = data["DeploymentArn"]
    if "DeploymentId" in data:
        out["deployment_id"] = data["DeploymentId"]
    if "DeploymentType" in data:
        import aws_sdk_greengrass.types.deployment_type

        out["deployment_type"] = (
            aws_sdk_greengrass.types.deployment_type.deserialize_json(
                data["DeploymentType"]
            )
        )
    if "GroupArn" in data:
        out["group_arn"] = data["GroupArn"]
    return out
