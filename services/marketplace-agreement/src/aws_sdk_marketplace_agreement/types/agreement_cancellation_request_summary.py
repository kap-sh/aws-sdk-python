"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementCancellationRequestSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.agreement_cancellation_request_id
    import aws_sdk_marketplace_agreement.types.agreement_cancellation_request_reason_code
    import aws_sdk_marketplace_agreement.types.agreement_cancellation_request_status
    import aws_sdk_marketplace_agreement.types.agreement_id
    import aws_sdk_marketplace_agreement.types.agreement_type
    import aws_sdk_marketplace_agreement.types.catalog
    import aws_sdk_marketplace_agreement.types.timestamp


class AgreementCancellationRequestSummary(TypedDict):
    agreement_cancellation_request_id: NotRequired[
        "aws_sdk_marketplace_agreement.types.agreement_cancellation_request_id.AgreementCancellationRequestId"
    ]
    """<p>The unique identifier of the cancellation request.</p>"""
    agreement_id: NotRequired[
        "aws_sdk_marketplace_agreement.types.agreement_id.AgreementId"
    ]
    """<p>The unique identifier of the agreement associated with this cancellation request.</p>"""
    status: NotRequired[
        "aws_sdk_marketplace_agreement.types.agreement_cancellation_request_status.AgreementCancellationRequestStatus"
    ]
    """<p>The current status of the cancellation request. Possible values include <code>PENDING_APPROVAL</code>, <code>APPROVED</code>, <code>REJECTED</code>, <code>CANCELLED</code>, and <code>VALIDATION_FAILED</code>.</p>"""
    reason_code: NotRequired[
        "aws_sdk_marketplace_agreement.types.agreement_cancellation_request_reason_code.AgreementCancellationRequestReasonCode"
    ]
    """<p>The reason code provided for the cancellation.</p>"""
    agreement_type: NotRequired[
        "aws_sdk_marketplace_agreement.types.agreement_type.AgreementType"
    ]
    """<p>The type of agreement.</p>"""
    catalog: NotRequired["aws_sdk_marketplace_agreement.types.catalog.Catalog"]
    """<p>The catalog in which the agreement was created.</p>"""
    created_at: NotRequired["aws_sdk_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The date and time when the cancellation request was created.</p>"""
    updated_at: NotRequired["aws_sdk_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The date and time when the cancellation request was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementCancellationRequestSummary) -> dict:
    out: dict = {}
    if "agreement_cancellation_request_id" in value:
        out["agreementCancellationRequestId"] = value[
            "agreement_cancellation_request_id"
        ]
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
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
    if "agreement_type" in value:
        out["agreementType"] = value["agreement_type"]
    if "catalog" in value:
        out["catalog"] = value["catalog"]
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


def deserialize_aws_json_1_0(data: dict) -> AgreementCancellationRequestSummary:
    out: AgreementCancellationRequestSummary = {}  # type: ignore[typeddict-item]
    if "agreementCancellationRequestId" in data:
        out["agreement_cancellation_request_id"] = data[
            "agreementCancellationRequestId"
        ]
    if "agreementId" in data:
        out["agreement_id"] = data["agreementId"]
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
    if "agreementType" in data:
        out["agreement_type"] = data["agreementType"]
    if "catalog" in data:
        out["catalog"] = data["catalog"]
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
