"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AcceptAgreementCancellationRequestInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.agreement_cancellation_request_id
    import aws_sdk_marketplace_agreement.types.agreement_id


class AcceptAgreementCancellationRequestInput(TypedDict, closed=True):
    agreement_id: "aws_sdk_marketplace_agreement.types.agreement_id.AgreementId"
    """<p>The unique identifier of the agreement associated with the cancellation request.</p>"""
    agreement_cancellation_request_id: "aws_sdk_marketplace_agreement.types.agreement_cancellation_request_id.AgreementCancellationRequestId"
    """<p>The unique identifier of the cancellation request to accept.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AcceptAgreementCancellationRequestInput) -> dict:
    out: dict = {}
    out["agreementId"] = value["agreement_id"]
    out["agreementCancellationRequestId"] = value["agreement_cancellation_request_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AcceptAgreementCancellationRequestInput:
    out: AcceptAgreementCancellationRequestInput = {}  # type: ignore[typeddict-item]
    if "agreementId" in data:
        out["agreement_id"] = data["agreementId"]
    else:
        raise DeserializationError(
            "AcceptAgreementCancellationRequestInput.agreement_id required"
        )
    if "agreementCancellationRequestId" in data:
        out["agreement_cancellation_request_id"] = data[
            "agreementCancellationRequestId"
        ]
    else:
        raise DeserializationError(
            "AcceptAgreementCancellationRequestInput.agreement_cancellation_request_id required"
        )
    return out
