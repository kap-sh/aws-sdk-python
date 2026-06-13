"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateFoundationModelAgreementRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.bedrock_model_id
    import aws_sdk_bedrock.types.offer_token


class CreateFoundationModelAgreementRequest(TypedDict):
    offer_token: "aws_sdk_bedrock.types.offer_token.OfferToken"
    """<p>An offer token encapsulates the information for an offer.</p>"""
    model_id: "aws_sdk_bedrock.types.bedrock_model_id.BedrockModelId"
    """<p>Model Id of the model for the access request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFoundationModelAgreementRequest) -> dict:
    out: dict = {}
    out["offerToken"] = value["offer_token"]
    out["modelId"] = value["model_id"]
    return out


def deserialize_json(data: dict) -> CreateFoundationModelAgreementRequest:
    out: CreateFoundationModelAgreementRequest = {}  # type: ignore[typeddict-item]
    if "offerToken" in data:
        out["offer_token"] = data["offerToken"]
    else:
        raise DeserializationError(
            "CreateFoundationModelAgreementRequest.offer_token required"
        )
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError(
            "CreateFoundationModelAgreementRequest.model_id required"
        )
    return out
