"""Generated from Smithy shape ``com.amazonaws.greengrass#GetBulkDeploymentStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class GetBulkDeploymentStatusRequest(TypedDict):
    bulk_deployment_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the bulk deployment."""


# --- restJson1 ser/de ---
def serialize_json(value: GetBulkDeploymentStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBulkDeploymentStatusRequest:
    out: GetBulkDeploymentStatusRequest = {}  # type: ignore[typeddict-item]
    return out
