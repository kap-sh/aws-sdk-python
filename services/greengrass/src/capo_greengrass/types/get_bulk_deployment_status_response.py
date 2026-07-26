"""Generated from Smithy shape ``com.amazonaws.greengrass#GetBulkDeploymentStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string
    import capo_greengrass.types.bulk_deployment_metrics
    import capo_greengrass.types.bulk_deployment_status
    import capo_greengrass.types.error_details
    import capo_greengrass.types.tags


class GetBulkDeploymentStatusResponse(TypedDict, closed=True):
    bulk_deployment_metrics: NotRequired[
        "capo_greengrass.types.bulk_deployment_metrics.BulkDeploymentMetrics"
    ]
    """Relevant metrics on input records processed during bulk deployment."""
    bulk_deployment_status: NotRequired[
        "capo_greengrass.types.bulk_deployment_status.BulkDeploymentStatus"
    ]
    """The status of the bulk deployment."""
    created_at: NotRequired["capo_greengrass.types.__string.__string"]
    """The time, in ISO format, when the deployment was created."""
    error_details: NotRequired["capo_greengrass.types.error_details.ErrorDetails"]
    """Error details"""
    error_message: NotRequired["capo_greengrass.types.__string.__string"]
    """Error message"""
    tags: NotRequired["capo_greengrass.types.tags.Tags"]
    """Tag(s) attached to the resource arn."""


# --- restJson1 ser/de ---
def serialize_json(value: GetBulkDeploymentStatusResponse) -> dict:
    out: dict = {}
    if "bulk_deployment_metrics" in value:
        import capo_greengrass.types.bulk_deployment_metrics

        out["BulkDeploymentMetrics"] = (
            capo_greengrass.types.bulk_deployment_metrics.serialize_json(
                value["bulk_deployment_metrics"]
            )
        )
    if "bulk_deployment_status" in value:
        import capo_greengrass.types.bulk_deployment_status

        out["BulkDeploymentStatus"] = (
            capo_greengrass.types.bulk_deployment_status.serialize_json(
                value["bulk_deployment_status"]
            )
        )
    if "created_at" in value:
        out["CreatedAt"] = value["created_at"]
    if "error_details" in value:
        import capo_greengrass.types.error_details

        out["ErrorDetails"] = capo_greengrass.types.error_details.serialize_json(
            value["error_details"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "tags" in value:
        import capo_greengrass.types.tags

        out["tags"] = capo_greengrass.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetBulkDeploymentStatusResponse:
    out: GetBulkDeploymentStatusResponse = {}  # type: ignore[typeddict-item]
    if "BulkDeploymentMetrics" in data:
        import capo_greengrass.types.bulk_deployment_metrics

        out["bulk_deployment_metrics"] = (
            capo_greengrass.types.bulk_deployment_metrics.deserialize_json(
                data["BulkDeploymentMetrics"]
            )
        )
    if "BulkDeploymentStatus" in data:
        import capo_greengrass.types.bulk_deployment_status

        out["bulk_deployment_status"] = (
            capo_greengrass.types.bulk_deployment_status.deserialize_json(
                data["BulkDeploymentStatus"]
            )
        )
    if "CreatedAt" in data:
        out["created_at"] = data["CreatedAt"]
    if "ErrorDetails" in data:
        import capo_greengrass.types.error_details

        out["error_details"] = capo_greengrass.types.error_details.deserialize_json(
            data["ErrorDetails"]
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "tags" in data:
        import capo_greengrass.types.tags

        out["tags"] = capo_greengrass.types.tags.deserialize_json(data["tags"])
    return out
