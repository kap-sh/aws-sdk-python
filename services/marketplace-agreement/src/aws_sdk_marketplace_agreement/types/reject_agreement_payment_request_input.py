"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#RejectAgreementPaymentRequestInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.agreement_id
    import aws_sdk_marketplace_agreement.types.payment_request_id
    import aws_sdk_marketplace_agreement.types.payment_request_rejection_reason


class RejectAgreementPaymentRequestInput(TypedDict, closed=True):
    payment_request_id: (
        "aws_sdk_marketplace_agreement.types.payment_request_id.PaymentRequestId"
    )
    """<p>The unique identifier of the payment request to reject.</p>"""
    agreement_id: "aws_sdk_marketplace_agreement.types.agreement_id.AgreementId"
    """<p>The unique identifier of the agreement associated with the payment request.</p>"""
    rejection_reason: NotRequired[
        "aws_sdk_marketplace_agreement.types.payment_request_rejection_reason.PaymentRequestRejectionReason"
    ]
    """<p>An optional reason for rejecting the payment request (1-250 characters). This message is visible to the seller.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RejectAgreementPaymentRequestInput) -> dict:
    out: dict = {}
    out["paymentRequestId"] = value["payment_request_id"]
    out["agreementId"] = value["agreement_id"]
    if "rejection_reason" in value:
        out["rejectionReason"] = value["rejection_reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RejectAgreementPaymentRequestInput:
    out: RejectAgreementPaymentRequestInput = {}  # type: ignore[typeddict-item]
    if "paymentRequestId" in data:
        out["payment_request_id"] = data["paymentRequestId"]
    else:
        raise DeserializationError(
            "RejectAgreementPaymentRequestInput.payment_request_id required"
        )
    if "agreementId" in data:
        out["agreement_id"] = data["agreementId"]
    else:
        raise DeserializationError(
            "RejectAgreementPaymentRequestInput.agreement_id required"
        )
    if "rejectionReason" in data:
        out["rejection_reason"] = data["rejectionReason"]
    return out
