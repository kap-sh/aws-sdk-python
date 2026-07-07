"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ListBillingAdjustmentRequestsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.agreement_id
    import aws_sdk_marketplace_agreement.types.agreement_type
    import aws_sdk_marketplace_agreement.types.billing_adjustment_status
    import aws_sdk_marketplace_agreement.types.catalog
    import aws_sdk_marketplace_agreement.types.max_results
    import aws_sdk_marketplace_agreement.types.next_token
    import aws_sdk_marketplace_agreement.types.timestamp


class ListBillingAdjustmentRequestsInput(TypedDict, closed=True):
    agreement_id: NotRequired[
        "aws_sdk_marketplace_agreement.types.agreement_id.AgreementId"
    ]
    """<p>The unique identifier of the agreement to list billing adjustment requests for.</p>"""
    status: NotRequired[
        "aws_sdk_marketplace_agreement.types.billing_adjustment_status.BillingAdjustmentStatus"
    ]
    """<p>An optional filter to return billing adjustment requests with the specified status.</p>"""
    created_after: NotRequired[
        "aws_sdk_marketplace_agreement.types.timestamp.Timestamp"
    ]
    """<p>An optional filter to return billing adjustment requests created after the specified timestamp.</p>"""
    created_before: NotRequired[
        "aws_sdk_marketplace_agreement.types.timestamp.Timestamp"
    ]
    """<p>An optional filter to return billing adjustment requests created before the specified timestamp.</p>"""
    max_results: NotRequired[
        "aws_sdk_marketplace_agreement.types.max_results.MaxResults"
    ]
    """<p>The maximum number of billing adjustment requests to return in the response.</p>"""
    catalog: NotRequired["aws_sdk_marketplace_agreement.types.catalog.Catalog"]
    """<p>An optional filter to return billing adjustment requests by catalog (e.g., <code>AWSMarketplace</code>).</p>"""
    agreement_type: NotRequired[
        "aws_sdk_marketplace_agreement.types.agreement_type.AgreementType"
    ]
    """<p>An optional filter to return billing adjustment requests by agreement type (e.g., <code>PurchaseAgreement</code>).</p>"""
    next_token: NotRequired["aws_sdk_marketplace_agreement.types.next_token.NextToken"]
    """<p>A token to specify where to start pagination.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBillingAdjustmentRequestsInput) -> dict:
    out: dict = {}
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    if "status" in value:
        import aws_sdk_marketplace_agreement.types.billing_adjustment_status

        out["status"] = (
            aws_sdk_marketplace_agreement.types.billing_adjustment_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "created_after" in value:
        import aws_sdk_marketplace_agreement.types.timestamp

        out["createdAfter"] = (
            aws_sdk_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["created_after"]
            )
        )
    if "created_before" in value:
        import aws_sdk_marketplace_agreement.types.timestamp

        out["createdBefore"] = (
            aws_sdk_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["created_before"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "catalog" in value:
        out["catalog"] = value["catalog"]
    if "agreement_type" in value:
        out["agreementType"] = value["agreement_type"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListBillingAdjustmentRequestsInput:
    out: ListBillingAdjustmentRequestsInput = {}  # type: ignore[typeddict-item]
    if "agreementId" in data:
        out["agreement_id"] = data["agreementId"]
    if "status" in data:
        import aws_sdk_marketplace_agreement.types.billing_adjustment_status

        out["status"] = (
            aws_sdk_marketplace_agreement.types.billing_adjustment_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "createdAfter" in data:
        import aws_sdk_marketplace_agreement.types.timestamp

        out["created_after"] = (
            aws_sdk_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["createdAfter"]
            )
        )
    if "createdBefore" in data:
        import aws_sdk_marketplace_agreement.types.timestamp

        out["created_before"] = (
            aws_sdk_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["createdBefore"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "catalog" in data:
        out["catalog"] = data["catalog"]
    if "agreementType" in data:
        out["agreement_type"] = data["agreementType"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
