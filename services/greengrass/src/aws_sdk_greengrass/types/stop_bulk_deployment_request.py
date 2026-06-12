"""Generated from Smithy shape ``com.amazonaws.greengrass#StopBulkDeploymentRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class StopBulkDeploymentRequest(TypedDict):
    bulk_deployment_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the bulk deployment."""


# --- restJson1 ser/de ---
def serialize_json(value: StopBulkDeploymentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopBulkDeploymentRequest:
    out: StopBulkDeploymentRequest = {}  # type: ignore[typeddict-item]
    return out
