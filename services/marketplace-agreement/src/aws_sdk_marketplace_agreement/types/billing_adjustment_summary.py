"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BillingAdjustmentSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.agreement_id
    import aws_sdk_marketplace_agreement.types.agreement_type
    import aws_sdk_marketplace_agreement.types.billing_adjustment_request_id
    import aws_sdk_marketplace_agreement.types.billing_adjustment_status
    import aws_sdk_marketplace_agreement.types.catalog
    import aws_sdk_marketplace_agreement.types.currency_code
    import aws_sdk_marketplace_agreement.types.invoice_id
    import aws_sdk_marketplace_agreement.types.positive_amount_upto8_decimals
    import aws_sdk_marketplace_agreement.types.timestamp


class BillingAdjustmentSummary(TypedDict):
    billing_adjustment_request_id: "aws_sdk_marketplace_agreement.types.billing_adjustment_request_id.BillingAdjustmentRequestId"
    """<p>The unique identifier of the billing adjustment request.</p>"""
    original_invoice_id: "aws_sdk_marketplace_agreement.types.invoice_id.InvoiceId"
    """<p>The identifier of the original invoice being adjusted.</p>"""
    adjustment_amount: "aws_sdk_marketplace_agreement.types.positive_amount_upto8_decimals.PositiveAmountUpto8Decimals"
    """<p>The adjustment amount as a string representation of a decimal number.</p>"""
    currency_code: "aws_sdk_marketplace_agreement.types.currency_code.CurrencyCode"
    """<p>The currency code for the adjustment amount.</p>"""
    status: "aws_sdk_marketplace_agreement.types.billing_adjustment_status.BillingAdjustmentStatus"
    """<p>The current status of the billing adjustment request.</p>"""
    agreement_id: "aws_sdk_marketplace_agreement.types.agreement_id.AgreementId"
    """<p>The unique identifier of the agreement associated with this billing adjustment request.</p>"""
    created_at: "aws_sdk_marketplace_agreement.types.timestamp.Timestamp"
    """<p>The date and time when the billing adjustment request was created.</p>"""
    updated_at: "aws_sdk_marketplace_agreement.types.timestamp.Timestamp"
    """<p>The date and time when the billing adjustment request was last updated.</p>"""
    agreement_type: "aws_sdk_marketplace_agreement.types.agreement_type.AgreementType"
    """<p>The type of agreement.</p>"""
    catalog: "aws_sdk_marketplace_agreement.types.catalog.Catalog"
    """<p>The catalog in which the agreement was created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingAdjustmentSummary) -> dict:
    out: dict = {}
    out["billingAdjustmentRequestId"] = value["billing_adjustment_request_id"]
    out["originalInvoiceId"] = value["original_invoice_id"]
    out["adjustmentAmount"] = value["adjustment_amount"]
    out["currencyCode"] = value["currency_code"]
    import aws_sdk_marketplace_agreement.types.billing_adjustment_status

    out["status"] = (
        aws_sdk_marketplace_agreement.types.billing_adjustment_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    out["agreementId"] = value["agreement_id"]
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
    out["agreementType"] = value["agreement_type"]
    out["catalog"] = value["catalog"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BillingAdjustmentSummary:
    out: BillingAdjustmentSummary = {}  # type: ignore[typeddict-item]
    if "billingAdjustmentRequestId" in data:
        out["billing_adjustment_request_id"] = data["billingAdjustmentRequestId"]
    else:
        raise DeserializationError(
            "BillingAdjustmentSummary.billing_adjustment_request_id required"
        )
    if "originalInvoiceId" in data:
        out["original_invoice_id"] = data["originalInvoiceId"]
    else:
        raise DeserializationError(
            "BillingAdjustmentSummary.original_invoice_id required"
        )
    if "adjustmentAmount" in data:
        out["adjustment_amount"] = data["adjustmentAmount"]
    else:
        raise DeserializationError(
            "BillingAdjustmentSummary.adjustment_amount required"
        )
    if "currencyCode" in data:
        out["currency_code"] = data["currencyCode"]
    else:
        raise DeserializationError("BillingAdjustmentSummary.currency_code required")
    if "status" in data:
        import aws_sdk_marketplace_agreement.types.billing_adjustment_status

        out["status"] = (
            aws_sdk_marketplace_agreement.types.billing_adjustment_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    else:
        raise DeserializationError("BillingAdjustmentSummary.status required")
    if "agreementId" in data:
        out["agreement_id"] = data["agreementId"]
    else:
        raise DeserializationError("BillingAdjustmentSummary.agreement_id required")
    if "createdAt" in data:
        import aws_sdk_marketplace_agreement.types.timestamp

        out["created_at"] = (
            aws_sdk_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("BillingAdjustmentSummary.created_at required")
    if "updatedAt" in data:
        import aws_sdk_marketplace_agreement.types.timestamp

        out["updated_at"] = (
            aws_sdk_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("BillingAdjustmentSummary.updated_at required")
    if "agreementType" in data:
        out["agreement_type"] = data["agreementType"]
    else:
        raise DeserializationError("BillingAdjustmentSummary.agreement_type required")
    if "catalog" in data:
        out["catalog"] = data["catalog"]
    else:
        raise DeserializationError("BillingAdjustmentSummary.catalog required")
    return out
