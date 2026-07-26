"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#GetAgreementCancellationRequestOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_cancellation_request_description
    import capo_marketplace_agreement.types.agreement_cancellation_request_id
    import capo_marketplace_agreement.types.agreement_cancellation_request_reason_code
    import capo_marketplace_agreement.types.agreement_cancellation_request_status
    import capo_marketplace_agreement.types.agreement_cancellation_request_status_message
    import capo_marketplace_agreement.types.agreement_id
    import capo_marketplace_agreement.types.timestamp


class GetAgreementCancellationRequestOutput(TypedDict, closed=True):
    agreement_cancellation_request_id: NotRequired[
        "capo_marketplace_agreement.types.agreement_cancellation_request_id.AgreementCancellationRequestId"
    ]
    """<p>The unique identifier of the cancellation request.</p>"""
    agreement_id: NotRequired[
        "capo_marketplace_agreement.types.agreement_id.AgreementId"
    ]
    """<p>The unique identifier of the agreement associated with this cancellation request. Use <code>DescribeAgreement</code> to retrieve full agreement details.</p>"""
    reason_code: NotRequired[
        "capo_marketplace_agreement.types.agreement_cancellation_request_reason_code.AgreementCancellationRequestReasonCode"
    ]
    """<p>The reason code provided for the cancellation.</p>"""
    description: NotRequired[
        "capo_marketplace_agreement.types.agreement_cancellation_request_description.AgreementCancellationRequestDescription"
    ]
    """<p>The detailed description of the cancellation reason, if provided.</p>"""
    status: NotRequired[
        "capo_marketplace_agreement.types.agreement_cancellation_request_status.AgreementCancellationRequestStatus"
    ]
    """<p>The current status of the cancellation request.</p>"""
    status_message: NotRequired[
        "capo_marketplace_agreement.types.agreement_cancellation_request_status_message.AgreementCancellationRequestStatusMessage"
    ]
    """<p>A message providing additional context about the cancellation request status.</p>"""
    created_at: NotRequired["capo_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The date and time when the cancellation request was created.</p>"""
    updated_at: NotRequired["capo_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The date and time when the cancellation request was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAgreementCancellationRequestOutput) -> dict:
    out: dict = {}
    if "agreement_cancellation_request_id" in value:
        out["agreementCancellationRequestId"] = value[
            "agreement_cancellation_request_id"
        ]
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    if "reason_code" in value:
        import capo_marketplace_agreement.types.agreement_cancellation_request_reason_code

        out["reasonCode"] = (
            capo_marketplace_agreement.types.agreement_cancellation_request_reason_code.serialize_aws_json_1_0(
                value["reason_code"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import capo_marketplace_agreement.types.agreement_cancellation_request_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_cancellation_request_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "created_at" in value:
        import capo_marketplace_agreement.types.timestamp

        out["createdAt"] = (
            capo_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import capo_marketplace_agreement.types.timestamp

        out["updatedAt"] = (
            capo_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["updated_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAgreementCancellationRequestOutput:
    out: GetAgreementCancellationRequestOutput = {}  # type: ignore[typeddict-item]
    if "agreementCancellationRequestId" in data:
        out["agreement_cancellation_request_id"] = data[
            "agreementCancellationRequestId"
        ]
    if "agreementId" in data:
        out["agreement_id"] = data["agreementId"]
    if "reasonCode" in data:
        import capo_marketplace_agreement.types.agreement_cancellation_request_reason_code

        out["reason_code"] = (
            capo_marketplace_agreement.types.agreement_cancellation_request_reason_code.deserialize_aws_json_1_0(
                data["reasonCode"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import capo_marketplace_agreement.types.agreement_cancellation_request_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_cancellation_request_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "createdAt" in data:
        import capo_marketplace_agreement.types.timestamp

        out["created_at"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import capo_marketplace_agreement.types.timestamp

        out["updated_at"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["updatedAt"]
            )
        )
    return out
