"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#GetBillingAdjustmentRequestOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.agreement_id
    import aws_sdk_marketplace_agreement.types.billing_adjustment_reason_code
    import aws_sdk_marketplace_agreement.types.billing_adjustment_request_id
    import aws_sdk_marketplace_agreement.types.billing_adjustment_status
    import aws_sdk_marketplace_agreement.types.billing_adjustment_status_message
    import aws_sdk_marketplace_agreement.types.currency_code
    import aws_sdk_marketplace_agreement.types.invoice_id
    import aws_sdk_marketplace_agreement.types.positive_amount_upto8_decimals
    import aws_sdk_marketplace_agreement.types.timestamp


class GetBillingAdjustmentRequestOutput(TypedDict, closed=True):
    billing_adjustment_request_id: "aws_sdk_marketplace_agreement.types.billing_adjustment_request_id.BillingAdjustmentRequestId"
    """<p>The unique identifier of the billing adjustment request.</p>"""
    agreement_id: "aws_sdk_marketplace_agreement.types.agreement_id.AgreementId"
    """<p>The unique identifier of the agreement associated with this billing adjustment request.</p>"""
    adjustment_reason_code: "aws_sdk_marketplace_agreement.types.billing_adjustment_reason_code.BillingAdjustmentReasonCode"
    """<p>The reason code for the billing adjustment.</p>"""
    description: NotRequired["str"]
    """<p>The detailed description of the billing adjustment reason, if provided.</p>"""
    original_invoice_id: "aws_sdk_marketplace_agreement.types.invoice_id.InvoiceId"
    """<p>The identifier of the original invoice being adjusted.</p>"""
    adjustment_amount: "aws_sdk_marketplace_agreement.types.positive_amount_upto8_decimals.PositiveAmountUpto8Decimals"
    """<p>The adjustment amount as a string representation of a decimal number.</p>"""
    currency_code: "aws_sdk_marketplace_agreement.types.currency_code.CurrencyCode"
    """<p>The currency code for the adjustment amount (e.g., <code>USD</code>).</p>"""
    status: "aws_sdk_marketplace_agreement.types.billing_adjustment_status.BillingAdjustmentStatus"
    """<p>The current status of the billing adjustment request.</p>"""
    status_message: NotRequired[
        "aws_sdk_marketplace_agreement.types.billing_adjustment_status_message.BillingAdjustmentStatusMessage"
    ]
    """<p>A message providing additional context about the billing adjustment request status. This field is populated only when the status is <code>VALIDATION_FAILED</code>.</p>"""
    created_at: "aws_sdk_marketplace_agreement.types.timestamp.Timestamp"
    """<p>The date and time when the billing adjustment request was created.</p>"""
    updated_at: "aws_sdk_marketplace_agreement.types.timestamp.Timestamp"
    """<p>The date and time when the billing adjustment request was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetBillingAdjustmentRequestOutput) -> dict:
    out: dict = {}
    out["billingAdjustmentRequestId"] = value["billing_adjustment_request_id"]
    out["agreementId"] = value["agreement_id"]
    import aws_sdk_marketplace_agreement.types.billing_adjustment_reason_code

    out["adjustmentReasonCode"] = (
        aws_sdk_marketplace_agreement.types.billing_adjustment_reason_code.serialize_aws_json_1_0(
            value["adjustment_reason_code"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    out["originalInvoiceId"] = value["original_invoice_id"]
    out["adjustmentAmount"] = value["adjustment_amount"]
    out["currencyCode"] = value["currency_code"]
    import aws_sdk_marketplace_agreement.types.billing_adjustment_status

    out["status"] = (
        aws_sdk_marketplace_agreement.types.billing_adjustment_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    import aws_sdk_marketplace_agreement.types.timestamp

    out["createdAt"] = (
        aws_sdk_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    )
    import aws_sdk_marketplace_agreement.types.timestamp

    out["updatedAt"] = (
        aws_sdk_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
            value["updated_at"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetBillingAdjustmentRequestOutput:
    out: GetBillingAdjustmentRequestOutput = {}  # type: ignore[typeddict-item]
    if "billingAdjustmentRequestId" in data:
        out["billing_adjustment_request_id"] = data["billingAdjustmentRequestId"]
    else:
        raise DeserializationError(
            "GetBillingAdjustmentRequestOutput.billing_adjustment_request_id required"
        )
    if "agreementId" in data:
        out["agreement_id"] = data["agreementId"]
    else:
        raise DeserializationError(
            "GetBillingAdjustmentRequestOutput.agreement_id required"
        )
    if "adjustmentReasonCode" in data:
        import aws_sdk_marketplace_agreement.types.billing_adjustment_reason_code

        out["adjustment_reason_code"] = (
            aws_sdk_marketplace_agreement.types.billing_adjustment_reason_code.deserialize_aws_json_1_0(
                data["adjustmentReasonCode"]
            )
        )
    else:
        raise DeserializationError(
            "GetBillingAdjustmentRequestOutput.adjustment_reason_code required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "originalInvoiceId" in data:
        out["original_invoice_id"] = data["originalInvoiceId"]
    else:
        raise DeserializationError(
            "GetBillingAdjustmentRequestOutput.original_invoice_id required"
        )
    if "adjustmentAmount" in data:
        out["adjustment_amount"] = data["adjustmentAmount"]
    else:
        raise DeserializationError(
            "GetBillingAdjustmentRequestOutput.adjustment_amount required"
        )
    if "currencyCode" in data:
        out["currency_code"] = data["currencyCode"]
    else:
        raise DeserializationError(
            "GetBillingAdjustmentRequestOutput.currency_code required"
        )
    if "status" in data:
        import aws_sdk_marketplace_agreement.types.billing_adjustment_status

        out["status"] = (
            aws_sdk_marketplace_agreement.types.billing_adjustment_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetBillingAdjustmentRequestOutput.status required")
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "createdAt" in data:
        import aws_sdk_marketplace_agreement.types.timestamp

        out["created_at"] = (
            aws_sdk_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError(
            "GetBillingAdjustmentRequestOutput.created_at required"
        )
    if "updatedAt" in data:
        import aws_sdk_marketplace_agreement.types.timestamp

        out["updated_at"] = (
            aws_sdk_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "GetBillingAdjustmentRequestOutput.updated_at required"
        )
    return out
