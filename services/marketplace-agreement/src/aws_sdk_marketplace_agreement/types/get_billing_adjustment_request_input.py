"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#GetBillingAdjustmentRequestInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.agreement_id
    import aws_sdk_marketplace_agreement.types.billing_adjustment_request_id


class GetBillingAdjustmentRequestInput(TypedDict):
    agreement_id: "aws_sdk_marketplace_agreement.types.agreement_id.AgreementId"
    """<p>The unique identifier of the agreement associated with the billing adjustment request.</p>"""
    billing_adjustment_request_id: "aws_sdk_marketplace_agreement.types.billing_adjustment_request_id.BillingAdjustmentRequestId"
    """<p>The unique identifier of the billing adjustment request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetBillingAdjustmentRequestInput) -> dict:
    out: dict = {}
    out["agreementId"] = value["agreement_id"]
    out["billingAdjustmentRequestId"] = value["billing_adjustment_request_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetBillingAdjustmentRequestInput:
    out: GetBillingAdjustmentRequestInput = {}  # type: ignore[typeddict-item]
    if "agreementId" in data:
        out["agreement_id"] = data["agreementId"]
    else:
        raise DeserializationError(
            "GetBillingAdjustmentRequestInput.agreement_id required"
        )
    if "billingAdjustmentRequestId" in data:
        out["billing_adjustment_request_id"] = data["billingAdjustmentRequestId"]
    else:
        raise DeserializationError(
            "GetBillingAdjustmentRequestInput.billing_adjustment_request_id required"
        )
    return out
