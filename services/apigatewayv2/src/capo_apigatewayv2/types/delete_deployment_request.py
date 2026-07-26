"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#DeleteDeploymentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string


class DeleteDeploymentRequest(TypedDict, closed=True):
    api_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    deployment_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The deployment ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDeploymentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDeploymentRequest:
    out: DeleteDeploymentRequest = {}  # type: ignore[typeddict-item]
    return out
