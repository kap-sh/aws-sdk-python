"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementInvoiceLineItemGroupSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.invoice_billing_period
    import aws_sdk_marketplace_agreement.types.invoice_type
    import aws_sdk_marketplace_agreement.types.invoicing_entity
    import aws_sdk_marketplace_agreement.types.pricing_currency_amount
    import aws_sdk_marketplace_agreement.types.resource_id
    import aws_sdk_marketplace_agreement.types.timestamp


class AgreementInvoiceLineItemGroupSummary(TypedDict):
    agreement_id: NotRequired[
        "aws_sdk_marketplace_agreement.types.resource_id.ResourceId"
    ]
    """<p>The unique identifier of the agreement.</p>"""
    invoice_id: NotRequired[
        "aws_sdk_marketplace_agreement.types.resource_id.ResourceId"
    ]
    """<p>The identifier of the invoice for this group.</p>"""
    pricing_currency_amount: NotRequired[
        "aws_sdk_marketplace_agreement.types.pricing_currency_amount.PricingCurrencyAmount"
    ]
    """<p>Monetary amounts for this invoice group.</p>"""
    invoice_billing_period: NotRequired[
        "aws_sdk_marketplace_agreement.types.invoice_billing_period.InvoiceBillingPeriod"
    ]
    """<p>The billing period associated with this group.</p>"""
    issued_time: NotRequired["aws_sdk_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The timestamp when the invoice containing this group was created.</p>"""
    invoice_type: NotRequired[
        "aws_sdk_marketplace_agreement.types.invoice_type.InvoiceType"
    ]
    """<p>The type of invoice. Valid values are <code>INVOICE</code> and <code>CREDIT_MEMO</code>.</p>"""
    invoicing_entity: NotRequired[
        "aws_sdk_marketplace_agreement.types.invoicing_entity.InvoicingEntity"
    ]
    """<p>The entity that issues the invoice.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementInvoiceLineItemGroupSummary) -> dict:
    out: dict = {}
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    if "invoice_id" in value:
        out["invoiceId"] = value["invoice_id"]
    if "pricing_currency_amount" in value:
        import aws_sdk_marketplace_agreement.types.pricing_currency_amount

        out["pricingCurrencyAmount"] = (
            aws_sdk_marketplace_agreement.types.pricing_currency_amount.serialize_aws_json_1_0(
                value["pricing_currency_amount"]
            )
        )
    if "invoice_billing_period" in value:
        import aws_sdk_marketplace_agreement.types.invoice_billing_period

        out["invoiceBillingPeriod"] = (
            aws_sdk_marketplace_agreement.types.invoice_billing_period.serialize_aws_json_1_0(
                value["invoice_billing_period"]
            )
        )
    if "issued_time" in value:
        import aws_sdk_marketplace_agreement.types.timestamp

        out["issuedTime"] = (
            aws_sdk_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["issued_time"]
            )
        )
    if "invoice_type" in value:
        import aws_sdk_marketplace_agreement.types.invoice_type

        out["invoiceType"] = (
            aws_sdk_marketplace_agreement.types.invoice_type.serialize_aws_json_1_0(
                value["invoice_type"]
            )
        )
    if "invoicing_entity" in value:
        import aws_sdk_marketplace_agreement.types.invoicing_entity

        out["invoicingEntity"] = (
            aws_sdk_marketplace_agreement.types.invoicing_entity.serialize_aws_json_1_0(
                value["invoicing_entity"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AgreementInvoiceLineItemGroupSummary:
    out: AgreementInvoiceLineItemGroupSummary = {}  # type: ignore[typeddict-item]
    if "agreementId" in data:
        out["agreement_id"] = data["agreementId"]
    if "invoiceId" in data:
        out["invoice_id"] = data["invoiceId"]
    if "pricingCurrencyAmount" in data:
        import aws_sdk_marketplace_agreement.types.pricing_currency_amount

        out["pricing_currency_amount"] = (
            aws_sdk_marketplace_agreement.types.pricing_currency_amount.deserialize_aws_json_1_0(
                data["pricingCurrencyAmount"]
            )
        )
    if "invoiceBillingPeriod" in data:
        import aws_sdk_marketplace_agreement.types.invoice_billing_period

        out["invoice_billing_period"] = (
            aws_sdk_marketplace_agreement.types.invoice_billing_period.deserialize_aws_json_1_0(
                data["invoiceBillingPeriod"]
            )
        )
    if "issuedTime" in data:
        import aws_sdk_marketplace_agreement.types.timestamp

        out["issued_time"] = (
            aws_sdk_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["issuedTime"]
            )
        )
    if "invoiceType" in data:
        import aws_sdk_marketplace_agreement.types.invoice_type

        out["invoice_type"] = (
            aws_sdk_marketplace_agreement.types.invoice_type.deserialize_aws_json_1_0(
                data["invoiceType"]
            )
        )
    if "invoicingEntity" in data:
        import aws_sdk_marketplace_agreement.types.invoicing_entity

        out["invoicing_entity"] = (
            aws_sdk_marketplace_agreement.types.invoicing_entity.deserialize_aws_json_1_0(
                data["invoicingEntity"]
            )
        )
    return out
