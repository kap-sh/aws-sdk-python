"""Generated from Smithy shape ``com.amazonaws.greengrass#ResetDeploymentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class ResetDeploymentsResponse(TypedDict, closed=True):
    deployment_arn: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ARN of the deployment."""
    deployment_id: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ID of the deployment."""


# --- restJson1 ser/de ---
def serialize_json(value: ResetDeploymentsResponse) -> dict:
    out: dict = {}
    if "deployment_arn" in value:
        out["DeploymentArn"] = value["deployment_arn"]
    if "deployment_id" in value:
        out["DeploymentId"] = value["deployment_id"]
    return out


def deserialize_json(data: dict) -> ResetDeploymentsResponse:
    out: ResetDeploymentsResponse = {}  # type: ignore[typeddict-item]
    if "DeploymentArn" in data:
        out["deployment_arn"] = data["DeploymentArn"]
    if "DeploymentId" in data:
        out["deployment_id"] = data["DeploymentId"]
    return out
