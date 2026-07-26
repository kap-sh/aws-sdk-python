"""Generated from Smithy shape ``com.amazonaws.greengrass#StartBulkDeploymentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string


class StartBulkDeploymentResponse(TypedDict, closed=True):
    bulk_deployment_arn: NotRequired["capo_greengrass.types.__string.__string"]
    """The ARN of the bulk deployment."""
    bulk_deployment_id: NotRequired["capo_greengrass.types.__string.__string"]
    """The ID of the bulk deployment."""


# --- restJson1 ser/de ---
def serialize_json(value: StartBulkDeploymentResponse) -> dict:
    out: dict = {}
    if "bulk_deployment_arn" in value:
        out["BulkDeploymentArn"] = value["bulk_deployment_arn"]
    if "bulk_deployment_id" in value:
        out["BulkDeploymentId"] = value["bulk_deployment_id"]
    return out


def deserialize_json(data: dict) -> StartBulkDeploymentResponse:
    out: StartBulkDeploymentResponse = {}  # type: ignore[typeddict-item]
    if "BulkDeploymentArn" in data:
        out["bulk_deployment_arn"] = data["BulkDeploymentArn"]
    if "BulkDeploymentId" in data:
        out["bulk_deployment_id"] = data["BulkDeploymentId"]
    return out
