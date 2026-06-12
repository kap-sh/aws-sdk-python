"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateCustomModelDeploymentResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.custom_model_deployment_arn


class CreateCustomModelDeploymentResponse(TypedDict):
    custom_model_deployment_arn: (
        "aws_sdk_bedrock.types.custom_model_deployment_arn.CustomModelDeploymentArn"
    )
    """<p>The Amazon Resource Name (ARN) of the custom model deployment. Use this ARN as the <code>modelId</code> parameter when invoking the model with the <code>InvokeModel</code> or <code>Converse</code> operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCustomModelDeploymentResponse) -> dict:
    out: dict = {}
    out["customModelDeploymentArn"] = value["custom_model_deployment_arn"]
    return out


def deserialize_json(data: dict) -> CreateCustomModelDeploymentResponse:
    out: CreateCustomModelDeploymentResponse = {}  # type: ignore[typeddict-item]
    if "customModelDeploymentArn" in data:
        out["custom_model_deployment_arn"] = data["customModelDeploymentArn"]
    else:
        raise DeserializationError(
            "CreateCustomModelDeploymentResponse.custom_model_deployment_arn required"
        )
    return out
