"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#GetAgreementTermsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.max_results
    import capo_marketplace_agreement.types.next_token
    import capo_marketplace_agreement.types.resource_id


class GetAgreementTermsInput(TypedDict, closed=True):
    agreement_id: "capo_marketplace_agreement.types.resource_id.ResourceId"
    """<p>The unique identifier of the agreement.</p>"""
    max_results: NotRequired["capo_marketplace_agreement.types.max_results.MaxResults"]
    """<p>The maximum number of agreements to return in the response.</p>"""
    next_token: NotRequired["capo_marketplace_agreement.types.next_token.NextToken"]
    """<p>A token to specify where to start pagination.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAgreementTermsInput) -> dict:
    out: dict = {}
    out["agreementId"] = value["agreement_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAgreementTermsInput:
    out: GetAgreementTermsInput = {}  # type: ignore[typeddict-item]
    if "agreementId" in data:
        out["agreement_id"] = data["agreementId"]
    else:
        raise DeserializationError("GetAgreementTermsInput.agreement_id required")
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
