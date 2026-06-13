"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#GetOfferTermsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.next_token
    import aws_sdk_marketplace_discovery.types.offer_terms_list


class GetOfferTermsOutput(TypedDict):
    offer_terms: "aws_sdk_marketplace_discovery.types.offer_terms_list.OfferTermsList"
    """<p>The terms attached to the offer. Each element contains exactly one term type.</p>"""
    next_token: NotRequired["aws_sdk_marketplace_discovery.types.next_token.NextToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOfferTermsOutput) -> dict:
    out: dict = {}
    import aws_sdk_marketplace_discovery.types.offer_terms_list

    out["offerTerms"] = (
        aws_sdk_marketplace_discovery.types.offer_terms_list.serialize_json(
            value["offer_terms"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetOfferTermsOutput:
    out: GetOfferTermsOutput = {}  # type: ignore[typeddict-item]
    if "offerTerms" in data:
        import aws_sdk_marketplace_discovery.types.offer_terms_list

        out["offer_terms"] = (
            aws_sdk_marketplace_discovery.types.offer_terms_list.deserialize_json(
                data["offerTerms"]
            )
        )
    else:
        raise DeserializationError("GetOfferTermsOutput.offer_terms required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
