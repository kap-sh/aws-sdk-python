"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AcceptAgreementPaymentRequestInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_id
    import capo_marketplace_agreement.types.payment_request_id
    import capo_marketplace_agreement.types.purchase_order_reference


class AcceptAgreementPaymentRequestInput(TypedDict, closed=True):
    payment_request_id: (
        "capo_marketplace_agreement.types.payment_request_id.PaymentRequestId"
    )
    """<p>The unique identifier of the payment request to accept.</p>"""
    agreement_id: "capo_marketplace_agreement.types.agreement_id.AgreementId"
    """<p>The unique identifier of the agreement associated with the payment request.</p>"""
    purchase_order_reference: NotRequired[
        "capo_marketplace_agreement.types.purchase_order_reference.PurchaseOrderReference"
    ]
    """<p>An optional purchase order reference that buyers can provide to associate the payment request with their internal purchase order system.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AcceptAgreementPaymentRequestInput) -> dict:
    out: dict = {}
    out["paymentRequestId"] = value["payment_request_id"]
    out["agreementId"] = value["agreement_id"]
    if "purchase_order_reference" in value:
        out["purchaseOrderReference"] = value["purchase_order_reference"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AcceptAgreementPaymentRequestInput:
    out: AcceptAgreementPaymentRequestInput = {}  # type: ignore[typeddict-item]
    if "paymentRequestId" in data:
        out["payment_request_id"] = data["paymentRequestId"]
    else:
        raise DeserializationError(
            "AcceptAgreementPaymentRequestInput.payment_request_id required"
        )
    if "agreementId" in data:
        out["agreement_id"] = data["agreementId"]
    else:
        raise DeserializationError(
            "AcceptAgreementPaymentRequestInput.agreement_id required"
        )
    if "purchaseOrderReference" in data:
        out["purchase_order_reference"] = data["purchaseOrderReference"]
    return out
