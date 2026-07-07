"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#GetAgreementCancellationRequestInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.agreement_cancellation_request_id
    import aws_sdk_marketplace_agreement.types.agreement_id


class GetAgreementCancellationRequestInput(TypedDict, closed=True):
    agreement_cancellation_request_id: "aws_sdk_marketplace_agreement.types.agreement_cancellation_request_id.AgreementCancellationRequestId"
    """<p>The unique identifier of the cancellation request.</p>"""
    agreement_id: "aws_sdk_marketplace_agreement.types.agreement_id.AgreementId"
    """<p>The unique identifier of the agreement associated with the cancellation request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAgreementCancellationRequestInput) -> dict:
    out: dict = {}
    out["agreementCancellationRequestId"] = value["agreement_cancellation_request_id"]
    out["agreementId"] = value["agreement_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAgreementCancellationRequestInput:
    out: GetAgreementCancellationRequestInput = {}  # type: ignore[typeddict-item]
    if "agreementCancellationRequestId" in data:
        out["agreement_cancellation_request_id"] = data[
            "agreementCancellationRequestId"
        ]
    else:
        raise DeserializationError(
            "GetAgreementCancellationRequestInput.agreement_cancellation_request_id required"
        )
    if "agreementId" in data:
        out["agreement_id"] = data["agreementId"]
    else:
        raise DeserializationError(
            "GetAgreementCancellationRequestInput.agreement_id required"
        )
    return out
