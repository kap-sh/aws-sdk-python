"""Generated from Smithy shape ``com.amazonaws.bedrock#ListFoundationModelAgreementOffersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.bedrock_model_id
    import capo_bedrock.types.offers


class ListFoundationModelAgreementOffersResponse(TypedDict, closed=True):
    model_id: "capo_bedrock.types.bedrock_model_id.BedrockModelId"
    """<p>Model Id of the foundation model.</p>"""
    offers: "capo_bedrock.types.offers.Offers"
    """<p>List of the offers associated with the specified model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFoundationModelAgreementOffersResponse) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    import capo_bedrock.types.offers

    out["offers"] = capo_bedrock.types.offers.serialize_json(value["offers"])
    return out


def deserialize_json(data: dict) -> ListFoundationModelAgreementOffersResponse:
    out: ListFoundationModelAgreementOffersResponse = {}  # type: ignore[typeddict-item]
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError(
            "ListFoundationModelAgreementOffersResponse.model_id required"
        )
    if "offers" in data:
        import capo_bedrock.types.offers

        out["offers"] = capo_bedrock.types.offers.deserialize_json(data["offers"])
    else:
        raise DeserializationError(
            "ListFoundationModelAgreementOffersResponse.offers required"
        )
    return out
