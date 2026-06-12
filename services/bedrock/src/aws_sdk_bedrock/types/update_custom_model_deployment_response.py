"""Generated from Smithy shape ``com.amazonaws.bedrock#UpdateCustomModelDeploymentResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.custom_model_deployment_arn


class UpdateCustomModelDeploymentResponse(TypedDict):
    custom_model_deployment_arn: (
        "aws_sdk_bedrock.types.custom_model_deployment_arn.CustomModelDeploymentArn"
    )
    """<p> ARN of the custom model deployment being updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCustomModelDeploymentResponse) -> dict:
    out: dict = {}
    out["customModelDeploymentArn"] = value["custom_model_deployment_arn"]
    return out


def deserialize_json(data: dict) -> UpdateCustomModelDeploymentResponse:
    out: UpdateCustomModelDeploymentResponse = {}  # type: ignore[typeddict-item]
    if "customModelDeploymentArn" in data:
        out["custom_model_deployment_arn"] = data["customModelDeploymentArn"]
    else:
        raise DeserializationError(
            "UpdateCustomModelDeploymentResponse.custom_model_deployment_arn required"
        )
    return out
