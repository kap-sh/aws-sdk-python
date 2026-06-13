"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ProposalSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.offer_id
    import aws_sdk_marketplace_agreement.types.offer_set_id
    import aws_sdk_marketplace_agreement.types.resources


class ProposalSummary(TypedDict):
    resources: NotRequired["aws_sdk_marketplace_agreement.types.resources.Resources"]
    """<p>The list of resources involved in the agreement.</p>"""
    offer_id: NotRequired["aws_sdk_marketplace_agreement.types.offer_id.OfferId"]
    """<p>The unique identifier of the offer in AWS Marketplace.</p>"""
    offer_set_id: NotRequired[
        "aws_sdk_marketplace_agreement.types.offer_set_id.OfferSetId"
    ]
    """<p>A unique identifier for the offer set containing this offer. All agreements created from offers in this set include this identifier as context.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProposalSummary) -> dict:
    out: dict = {}
    if "resources" in value:
        import aws_sdk_marketplace_agreement.types.resources

        out["resources"] = (
            aws_sdk_marketplace_agreement.types.resources.serialize_aws_json_1_0(
                value["resources"]
            )
        )
    if "offer_id" in value:
        out["offerId"] = value["offer_id"]
    if "offer_set_id" in value:
        out["offerSetId"] = value["offer_set_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ProposalSummary:
    out: ProposalSummary = {}  # type: ignore[typeddict-item]
    if "resources" in data:
        import aws_sdk_marketplace_agreement.types.resources

        out["resources"] = (
            aws_sdk_marketplace_agreement.types.resources.deserialize_aws_json_1_0(
                data["resources"]
            )
        )
    if "offerId" in data:
        out["offer_id"] = data["offerId"]
    if "offerSetId" in data:
        out["offer_set_id"] = data["offerSetId"]
    return out
