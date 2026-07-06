"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#GetAgreementPaymentRequestInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.agreement_id
    import aws_sdk_marketplace_agreement.types.payment_request_id


class GetAgreementPaymentRequestInput(TypedDict, closed=True):
    payment_request_id: (
        "aws_sdk_marketplace_agreement.types.payment_request_id.PaymentRequestId"
    )
    """<p>The identifier of the payment request.</p>"""
    agreement_id: "aws_sdk_marketplace_agreement.types.agreement_id.AgreementId"
    """<p>The unique identifier of the agreement associated with the payment request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAgreementPaymentRequestInput) -> dict:
    out: dict = {}
    out["paymentRequestId"] = value["payment_request_id"]
    out["agreementId"] = value["agreement_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAgreementPaymentRequestInput:
    out: GetAgreementPaymentRequestInput = {}  # type: ignore[typeddict-item]
    if "paymentRequestId" in data:
        out["payment_request_id"] = data["paymentRequestId"]
    else:
        raise DeserializationError(
            "GetAgreementPaymentRequestInput.payment_request_id required"
        )
    if "agreementId" in data:
        out["agreement_id"] = data["agreementId"]
    else:
        raise DeserializationError(
            "GetAgreementPaymentRequestInput.agreement_id required"
        )
    return out
