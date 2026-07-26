"""Generated from Smithy shape ``com.amazonaws.greengrass#GetDeploymentStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string


class GetDeploymentStatusRequest(TypedDict, closed=True):
    deployment_id: "capo_greengrass.types.__string.__string"
    """The ID of the deployment."""
    group_id: "capo_greengrass.types.__string.__string"
    """The ID of the Greengrass group."""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeploymentStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDeploymentStatusRequest:
    out: GetDeploymentStatusRequest = {}  # type: ignore[typeddict-item]
    return out
