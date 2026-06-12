"""Generated from Smithy shape ``com.amazonaws.bedrock#ListFoundationModelAgreementOffersRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.bedrock_model_id
    import aws_sdk_bedrock.types.offer_type


class ListFoundationModelAgreementOffersRequest(TypedDict):
    model_id: "aws_sdk_bedrock.types.bedrock_model_id.BedrockModelId"
    """<p>Model Id of the foundation model.</p>"""
    offer_type: NotRequired["aws_sdk_bedrock.types.offer_type.OfferType"]
    """<p>Type of offer associated with the model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFoundationModelAgreementOffersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFoundationModelAgreementOffersRequest:
    out: ListFoundationModelAgreementOffersRequest = {}  # type: ignore[typeddict-item]
    return out
