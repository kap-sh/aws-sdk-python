"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#GetOfferTermsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.next_token
    import aws_sdk_marketplace_discovery.types.offer_id


class GetOfferTermsInput(TypedDict):
    offer_id: "aws_sdk_marketplace_discovery.types.offer_id.OfferId"
    """<p>The unique identifier of the offer whose terms to retrieve.</p>"""
    max_results: "int"
    """<p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to get more results.</p>"""
    next_token: NotRequired["aws_sdk_marketplace_discovery.types.next_token.NextToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOfferTermsInput) -> dict:
    out: dict = {}
    out["offerId"] = value["offer_id"]
    out["maxResults"] = value.get("max_results", 10)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetOfferTermsInput:
    out: GetOfferTermsInput = {}  # type: ignore[typeddict-item]
    if "offerId" in data:
        out["offer_id"] = data["offerId"]
    else:
        raise DeserializationError("GetOfferTermsInput.offer_id required")
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 10
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
