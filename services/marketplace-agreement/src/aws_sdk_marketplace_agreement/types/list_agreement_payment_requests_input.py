"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ListAgreementPaymentRequestsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.agreement_id
    import aws_sdk_marketplace_agreement.types.agreement_type
    import aws_sdk_marketplace_agreement.types.catalog
    import aws_sdk_marketplace_agreement.types.max_results
    import aws_sdk_marketplace_agreement.types.next_token
    import aws_sdk_marketplace_agreement.types.party_type
    import aws_sdk_marketplace_agreement.types.payment_request_status


class ListAgreementPaymentRequestsInput(TypedDict):
    party_type: "aws_sdk_marketplace_agreement.types.party_type.PartyType"
    """<p>The party type for the payment requests. Required parameter. Use <code>Proposer</code> to list payment requests where you are the seller, or <code>Acceptor</code> to list payment requests where you are the buyer.</p>"""
    agreement_type: NotRequired[
        "aws_sdk_marketplace_agreement.types.agreement_type.AgreementType"
    ]
    """<p>An optional parameter to list payment requests by agreement type (e.g., <code>PurchaseAgreement</code>).</p>"""
    catalog: NotRequired["aws_sdk_marketplace_agreement.types.catalog.Catalog"]
    """<p>An optional parameter to list payment requests by catalog (e.g., <code>AWSMarketplace</code>).</p>"""
    agreement_id: NotRequired[
        "aws_sdk_marketplace_agreement.types.agreement_id.AgreementId"
    ]
    """<p>An optional parameter to list payment requests for a specific agreement.</p>"""
    status: NotRequired[
        "aws_sdk_marketplace_agreement.types.payment_request_status.PaymentRequestStatus"
    ]
    """<p>An optional parameter to list payment requests by status. Valid values include <code>VALIDATING</code>, <code>VALIDATION_FAILED</code>, <code>PENDING_APPROVAL</code>, <code>APPROVED</code>, <code>REJECTED</code>, and <code>CANCELLED</code>.</p>"""
    max_results: NotRequired[
        "aws_sdk_marketplace_agreement.types.max_results.MaxResults"
    ]
    """<p>The maximum number of payment requests to return in a single response (1-50). Default is 50.</p>"""
    next_token: NotRequired["aws_sdk_marketplace_agreement.types.next_token.NextToken"]
    """<p>A token to specify where to start pagination.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAgreementPaymentRequestsInput) -> dict:
    out: dict = {}
    out["partyType"] = value["party_type"]
    if "agreement_type" in value:
        out["agreementType"] = value["agreement_type"]
    if "catalog" in value:
        out["catalog"] = value["catalog"]
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    if "status" in value:
        import aws_sdk_marketplace_agreement.types.payment_request_status

        out["status"] = (
            aws_sdk_marketplace_agreement.types.payment_request_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAgreementPaymentRequestsInput:
    out: ListAgreementPaymentRequestsInput = {}  # type: ignore[typeddict-item]
    if "partyType" in data:
        out["party_type"] = data["partyType"]
    else:
        raise DeserializationError(
            "ListAgreementPaymentRequestsInput.party_type required"
        )
    if "agreementType" in data:
        out["agreement_type"] = data["agreementType"]
    if "catalog" in data:
        out["catalog"] = data["catalog"]
    if "agreementId" in data:
        out["agreement_id"] = data["agreementId"]
    if "status" in data:
        import aws_sdk_marketplace_agreement.types.payment_request_status

        out["status"] = (
            aws_sdk_marketplace_agreement.types.payment_request_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
