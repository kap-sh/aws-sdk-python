"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#DeleteDeploymentRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class DeleteDeploymentRequest(TypedDict):
    api_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    deployment_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The deployment ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDeploymentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDeploymentRequest:
    out: DeleteDeploymentRequest = {}  # type: ignore[typeddict-item]
    return out
