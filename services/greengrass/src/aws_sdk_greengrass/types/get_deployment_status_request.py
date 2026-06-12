"""Generated from Smithy shape ``com.amazonaws.greengrass#GetDeploymentStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class GetDeploymentStatusRequest(TypedDict):
    deployment_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the deployment."""
    group_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the Greengrass group."""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeploymentStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDeploymentStatusRequest:
    out: GetDeploymentStatusRequest = {}  # type: ignore[typeddict-item]
    return out
