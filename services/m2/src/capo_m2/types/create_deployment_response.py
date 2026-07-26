"""Generated from Smithy shape ``com.amazonaws.m2#CreateDeploymentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_m2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_m2.types.identifier


class CreateDeploymentResponse(TypedDict, closed=True):
    deployment_id: "capo_m2.types.identifier.Identifier"
    """<p>The unique identifier of the deployment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDeploymentResponse) -> dict:
    out: dict = {}
    out["deploymentId"] = value["deployment_id"]
    return out


def deserialize_json(data: dict) -> CreateDeploymentResponse:
    out: CreateDeploymentResponse = {}  # type: ignore[typeddict-item]
    if "deploymentId" in data:
        out["deployment_id"] = data["deploymentId"]
    else:
        raise DeserializationError("CreateDeploymentResponse.deployment_id required")
    return out
