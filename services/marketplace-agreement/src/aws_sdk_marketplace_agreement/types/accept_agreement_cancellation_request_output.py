"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AcceptAgreementCancellationRequestOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.agreement_cancellation_request_description
    import aws_sdk_marketplace_agreement.types.agreement_cancellation_request_id
    import aws_sdk_marketplace_agreement.types.agreement_cancellation_request_reason_code
    import aws_sdk_marketplace_agreement.types.agreement_cancellation_request_status
    import aws_sdk_marketplace_agreement.types.agreement_id
    import aws_sdk_marketplace_agreement.types.timestamp


class AcceptAgreementCancellationRequestOutput(TypedDict):
    agreement_id: NotRequired[
        "aws_sdk_marketplace_agreement.types.agreement_id.AgreementId"
    ]
    """<p>The unique identifier of the agreement associated with this cancellation request.</p>"""
    agreement_cancellation_request_id: NotRequired[
        "aws_sdk_marketplace_agreement.types.agreement_cancellation_request_id.AgreementCancellationRequestId"
    ]
    """<p>The unique identifier of the accepted cancellation request.</p>"""
    status: NotRequired[
        "aws_sdk_marketplace_agreement.types.agreement_cancellation_request_status.AgreementCancellationRequestStatus"
    ]
    """<p>The updated status of the cancellation request, which is <code>APPROVED</code>.</p>"""
    reason_code: NotRequired[
        "aws_sdk_marketplace_agreement.types.agreement_cancellation_request_reason_code.AgreementCancellationRequestReasonCode"
    ]
    """<p>The original reason code provided when the cancellation request was created.</p>"""
    description: NotRequired[
        "aws_sdk_marketplace_agreement.types.agreement_cancellation_request_description.AgreementCancellationRequestDescription"
    ]
    """<p>The detailed description of the cancellation reason, if provided.</p>"""
    created_at: NotRequired["aws_sdk_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The date and time when the cancellation request was originally created.</p>"""
    updated_at: NotRequired["aws_sdk_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The date and time when the cancellation request was accepted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AcceptAgreementCancellationRequestOutput) -> dict:
    out: dict = {}
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    if "agreement_cancellation_request_id" in value:
        out["agreementCancellationRequestId"] = value[
            "agreement_cancellation_request_id"
        ]
    if "status" in value:
        import aws_sdk_marketplace_agreement.types.agreement_cancellation_request_status

        out["status"] = (
            aws_sdk_marketplace_agreement.types.agreement_cancellation_request_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "reason_code" in value:
        import aws_sdk_marketplace_agreement.types.agreement_cancellation_request_reason_code

        out["reasonCode"] = (
            aws_sdk_marketplace_agreement.types.agreement_cancellation_request_reason_code.serialize_aws_json_1_0(
                value["reason_code"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "created_at" in value:
        import aws_sdk_marketplace_agreement.types.timestamp

        out["createdAt"] = (
            aws_sdk_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_marketplace_agreement.types.timestamp

        out["updatedAt"] = (
            aws_sdk_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["updated_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AcceptAgreementCancellationRequestOutput:
    out: AcceptAgreementCancellationRequestOutput = {}  # type: ignore[typeddict-item]
    if "agreementId" in data:
        out["agreement_id"] = data["agreementId"]
    if "agreementCancellationRequestId" in data:
        out["agreement_cancellation_request_id"] = data[
            "agreementCancellationRequestId"
        ]
    if "status" in data:
        import aws_sdk_marketplace_agreement.types.agreement_cancellation_request_status

        out["status"] = (
            aws_sdk_marketplace_agreement.types.agreement_cancellation_request_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "reasonCode" in data:
        import aws_sdk_marketplace_agreement.types.agreement_cancellation_request_reason_code

        out["reason_code"] = (
            aws_sdk_marketplace_agreement.types.agreement_cancellation_request_reason_code.deserialize_aws_json_1_0(
                data["reasonCode"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "createdAt" in data:
        import aws_sdk_marketplace_agreement.types.timestamp

        out["created_at"] = (
            aws_sdk_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_marketplace_agreement.types.timestamp

        out["updated_at"] = (
            aws_sdk_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["updatedAt"]
            )
        )
    return out
