"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#CancelAgreementCancellationRequestInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.agreement_cancellation_request_cancellation_reason
    import aws_sdk_marketplace_agreement.types.agreement_cancellation_request_id
    import aws_sdk_marketplace_agreement.types.agreement_id


class CancelAgreementCancellationRequestInput(TypedDict):
    agreement_id: "aws_sdk_marketplace_agreement.types.agreement_id.AgreementId"
    """<p>The unique identifier of the agreement associated with the cancellation request.</p>"""
    agreement_cancellation_request_id: "aws_sdk_marketplace_agreement.types.agreement_cancellation_request_id.AgreementCancellationRequestId"
    """<p>The unique identifier of the cancellation request to cancel.</p>"""
    cancellation_reason: "aws_sdk_marketplace_agreement.types.agreement_cancellation_request_cancellation_reason.AgreementCancellationRequestCancellationReason"
    """<p>A required message explaining why the cancellation request is being withdrawn (1-2000 characters).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelAgreementCancellationRequestInput) -> dict:
    out: dict = {}
    out["agreementId"] = value["agreement_id"]
    out["agreementCancellationRequestId"] = value["agreement_cancellation_request_id"]
    out["cancellationReason"] = value["cancellation_reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelAgreementCancellationRequestInput:
    out: CancelAgreementCancellationRequestInput = {}  # type: ignore[typeddict-item]
    if "agreementId" in data:
        out["agreement_id"] = data["agreementId"]
    else:
        raise DeserializationError(
            "CancelAgreementCancellationRequestInput.agreement_id required"
        )
    if "agreementCancellationRequestId" in data:
        out["agreement_cancellation_request_id"] = data[
            "agreementCancellationRequestId"
        ]
    else:
        raise DeserializationError(
            "CancelAgreementCancellationRequestInput.agreement_cancellation_request_id required"
        )
    if "cancellationReason" in data:
        out["cancellation_reason"] = data["cancellationReason"]
    else:
        raise DeserializationError(
            "CancelAgreementCancellationRequestInput.cancellation_reason required"
        )
    return out
