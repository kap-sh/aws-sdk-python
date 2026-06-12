"""Generated from Smithy shape ``com.amazonaws.bedrock#GetCustomModelDeploymentRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.custom_model_deployment_identifier


class GetCustomModelDeploymentRequest(TypedDict):
    custom_model_deployment_identifier: "aws_sdk_bedrock.types.custom_model_deployment_identifier.CustomModelDeploymentIdentifier"
    """<p>The Amazon Resource Name (ARN) or name of the custom model deployment to retrieve information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCustomModelDeploymentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCustomModelDeploymentRequest:
    out: GetCustomModelDeploymentRequest = {}  # type: ignore[typeddict-item]
    return out
