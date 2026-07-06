"""Generated from Smithy shape ``com.amazonaws.apigateway#DeleteDeploymentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class DeleteDeploymentRequest(TypedDict, closed=True):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    deployment_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The identifier of the Deployment resource to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDeploymentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDeploymentRequest:
    out: DeleteDeploymentRequest = {}  # type: ignore[typeddict-item]
    return out
