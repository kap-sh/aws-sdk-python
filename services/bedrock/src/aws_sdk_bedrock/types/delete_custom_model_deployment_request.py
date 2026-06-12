"""Generated from Smithy shape ``com.amazonaws.bedrock#DeleteCustomModelDeploymentRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.custom_model_deployment_identifier


class DeleteCustomModelDeploymentRequest(TypedDict):
    custom_model_deployment_identifier: "aws_sdk_bedrock.types.custom_model_deployment_identifier.CustomModelDeploymentIdentifier"
    """<p>The Amazon Resource Name (ARN) or name of the custom model deployment to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCustomModelDeploymentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCustomModelDeploymentRequest:
    out: DeleteCustomModelDeploymentRequest = {}  # type: ignore[typeddict-item]
    return out
