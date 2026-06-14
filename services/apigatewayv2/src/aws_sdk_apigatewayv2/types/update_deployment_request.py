"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#UpdateDeploymentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string
    import aws_sdk_apigatewayv2.types.string_with_length_between0_and1024


class UpdateDeploymentRequest(TypedDict):
    api_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    deployment_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The deployment ID.</p>"""
    description: NotRequired[
        "aws_sdk_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
    ]
    """<p>The description for the deployment resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDeploymentRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateDeploymentRequest:
    out: UpdateDeploymentRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    return out
