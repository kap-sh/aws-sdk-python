"""Generated from Smithy shape ``com.amazonaws.m2#GetDeploymentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_m2.types.identifier


class GetDeploymentRequest(TypedDict, closed=True):
    deployment_id: "capo_m2.types.identifier.Identifier"
    """<p>The unique identifier for the deployment.</p>"""
    application_id: "capo_m2.types.identifier.Identifier"
    """<p>The unique identifier of the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeploymentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDeploymentRequest:
    out: GetDeploymentRequest = {}  # type: ignore[typeddict-item]
    return out
