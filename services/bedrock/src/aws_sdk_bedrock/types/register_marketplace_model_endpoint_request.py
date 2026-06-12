"""Generated from Smithy shape ``com.amazonaws.bedrock#RegisterMarketplaceModelEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.arn
    import aws_sdk_bedrock.types.model_source_identifier


class RegisterMarketplaceModelEndpointRequest(TypedDict):
    endpoint_identifier: "aws_sdk_bedrock.types.arn.Arn"
    """<p>The ARN of the Amazon SageMaker endpoint you want to register with Amazon Bedrock Marketplace.</p>"""
    model_source_identifier: (
        "aws_sdk_bedrock.types.model_source_identifier.ModelSourceIdentifier"
    )
    """<p>The ARN of the model from Amazon Bedrock Marketplace that is deployed on the endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterMarketplaceModelEndpointRequest) -> dict:
    out: dict = {}
    out["modelSourceIdentifier"] = value["model_source_identifier"]
    return out


def deserialize_json(data: dict) -> RegisterMarketplaceModelEndpointRequest:
    out: RegisterMarketplaceModelEndpointRequest = {}  # type: ignore[typeddict-item]
    if "modelSourceIdentifier" in data:
        out["model_source_identifier"] = data["modelSourceIdentifier"]
    else:
        raise DeserializationError(
            "RegisterMarketplaceModelEndpointRequest.model_source_identifier required"
        )
    return out
