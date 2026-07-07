"""Generated from Smithy shape ``com.amazonaws.invoicing#InvoiceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_invoicing.types.account_id_string
    import aws_sdk_invoicing.types.basic_string
    import aws_sdk_invoicing.types.bill_source_account_list
    import aws_sdk_invoicing.types.bill_type
    import aws_sdk_invoicing.types.billing_period
    import aws_sdk_invoicing.types.einvoice_delivery_status
    import aws_sdk_invoicing.types.entity
    import aws_sdk_invoicing.types.invoice_currency_amount
    import aws_sdk_invoicing.types.invoice_frequency
    import aws_sdk_invoicing.types.invoice_type
    import aws_sdk_invoicing.types.receiver_role
    import aws_sdk_invoicing.types.tax_authority_status


class InvoiceSummary(TypedDict, closed=True):
    account_id: NotRequired["aws_sdk_invoicing.types.account_id_string.AccountIdString"]
    """<p> The Amazon Web Services account ID. </p>"""
    invoice_id: NotRequired["aws_sdk_invoicing.types.basic_string.BasicString"]
    """<p> The invoice ID. </p>"""
    issued_date: NotRequired["datetime.datetime"]
    """<p> The issued date of the invoice. </p>"""
    due_date: NotRequired["datetime.datetime"]
    """<p> The invoice due date. </p>"""
    bill_source_accounts: NotRequired[
        "aws_sdk_invoicing.types.bill_source_account_list.BillSourceAccountList"
    ]
    """<p> The list of Amazon Web Services account IDs that are the bill source of the invoice. Currently, only a single bill source account is returned.</p>"""
    bill_source_accounts_total_count: NotRequired["int"]
    """<p> The total number of accounts that are the bill source of the invoice. </p>"""
    receiver_role: NotRequired["aws_sdk_invoicing.types.receiver_role.ReceiverRole"]
    """<p>The role of the invoice receiver.</p>"""
    entity: NotRequired["aws_sdk_invoicing.types.entity.Entity"]
    """<p>The organization name providing Amazon Web Services services.</p>"""
    billing_period: NotRequired["aws_sdk_invoicing.types.billing_period.BillingPeriod"]
    """<p> The billing period of the invoice-related document. </p>"""
    invoice_frequency: NotRequired[
        "aws_sdk_invoicing.types.invoice_frequency.InvoiceFrequency"
    ]
    """<p> The frequency of the invoice. </p>"""
    bill_type: NotRequired["aws_sdk_invoicing.types.bill_type.BillType"]
    """<p> The type of the bill. </p>"""
    invoice_type: NotRequired["aws_sdk_invoicing.types.invoice_type.InvoiceType"]
    """<p> The type of invoice. </p>"""
    commercial_invoice_id: NotRequired[
        "aws_sdk_invoicing.types.basic_string.BasicString"
    ]
    """<p> The commercial invoice ID. This is only applicable for tax invoices and identifies the associated commercial invoice. </p>"""
    original_invoice_id: NotRequired["aws_sdk_invoicing.types.basic_string.BasicString"]
    """<p>The initial or original invoice ID. </p>"""
    purchase_order_number: NotRequired[
        "aws_sdk_invoicing.types.basic_string.BasicString"
    ]
    """<p> The purchase order number associated to the invoice.</p>"""
    einvoice_delivery_status: NotRequired[
        "aws_sdk_invoicing.types.einvoice_delivery_status.EinvoiceDeliveryStatus"
    ]
    """<p> The e-invoice delivery status. </p>"""
    tax_authority_status: NotRequired[
        "aws_sdk_invoicing.types.tax_authority_status.TaxAuthorityStatus"
    ]
    """<p> The current status of an invoice as reported to the tax authority. This captures scenarios where an invoice may be cancelled after issuance. </p>"""
    base_currency_amount: NotRequired[
        "aws_sdk_invoicing.types.invoice_currency_amount.InvoiceCurrencyAmount"
    ]
    """<p> The summary with the product and service currency. </p>"""
    tax_currency_amount: NotRequired[
        "aws_sdk_invoicing.types.invoice_currency_amount.InvoiceCurrencyAmount"
    ]
    """<p> The summary with the tax currency. </p>"""
    payment_currency_amount: NotRequired[
        "aws_sdk_invoicing.types.invoice_currency_amount.InvoiceCurrencyAmount"
    ]
    """<p> The summary with the customer configured currency. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvoiceSummary) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "invoice_id" in value:
        out["InvoiceId"] = value["invoice_id"]
    if "issued_date" in value:
        import aws_sdk_invoicing.types._prelude.timestamp

        out["IssuedDate"] = (
            aws_sdk_invoicing.types._prelude.timestamp.serialize_aws_json_1_0(
                value["issued_date"]
            )
        )
    if "due_date" in value:
        import aws_sdk_invoicing.types._prelude.timestamp

        out["DueDate"] = (
            aws_sdk_invoicing.types._prelude.timestamp.serialize_aws_json_1_0(
                value["due_date"]
            )
        )
    if "bill_source_accounts" in value:
        import aws_sdk_invoicing.types.bill_source_account_list

        out["BillSourceAccounts"] = (
            aws_sdk_invoicing.types.bill_source_account_list.serialize_aws_json_1_0(
                value["bill_source_accounts"]
            )
        )
    if "bill_source_accounts_total_count" in value:
        out["BillSourceAccountsTotalCount"] = value["bill_source_accounts_total_count"]
    if "receiver_role" in value:
        import aws_sdk_invoicing.types.receiver_role

        out["ReceiverRole"] = (
            aws_sdk_invoicing.types.receiver_role.serialize_aws_json_1_0(
                value["receiver_role"]
            )
        )
    if "entity" in value:
        import aws_sdk_invoicing.types.entity

        out["Entity"] = aws_sdk_invoicing.types.entity.serialize_aws_json_1_0(
            value["entity"]
        )
    if "billing_period" in value:
        import aws_sdk_invoicing.types.billing_period

        out["BillingPeriod"] = (
            aws_sdk_invoicing.types.billing_period.serialize_aws_json_1_0(
                value["billing_period"]
            )
        )
    if "invoice_frequency" in value:
        import aws_sdk_invoicing.types.invoice_frequency

        out["InvoiceFrequency"] = (
            aws_sdk_invoicing.types.invoice_frequency.serialize_aws_json_1_0(
                value["invoice_frequency"]
            )
        )
    if "bill_type" in value:
        import aws_sdk_invoicing.types.bill_type

        out["BillType"] = aws_sdk_invoicing.types.bill_type.serialize_aws_json_1_0(
            value["bill_type"]
        )
    if "invoice_type" in value:
        import aws_sdk_invoicing.types.invoice_type

        out["InvoiceType"] = (
            aws_sdk_invoicing.types.invoice_type.serialize_aws_json_1_0(
                value["invoice_type"]
            )
        )
    if "commercial_invoice_id" in value:
        out["CommercialInvoiceId"] = value["commercial_invoice_id"]
    if "original_invoice_id" in value:
        out["OriginalInvoiceId"] = value["original_invoice_id"]
    if "purchase_order_number" in value:
        out["PurchaseOrderNumber"] = value["purchase_order_number"]
    if "einvoice_delivery_status" in value:
        import aws_sdk_invoicing.types.einvoice_delivery_status

        out["EinvoiceDeliveryStatus"] = (
            aws_sdk_invoicing.types.einvoice_delivery_status.serialize_aws_json_1_0(
                value["einvoice_delivery_status"]
            )
        )
    if "tax_authority_status" in value:
        import aws_sdk_invoicing.types.tax_authority_status

        out["TaxAuthorityStatus"] = (
            aws_sdk_invoicing.types.tax_authority_status.serialize_aws_json_1_0(
                value["tax_authority_status"]
            )
        )
    if "base_currency_amount" in value:
        import aws_sdk_invoicing.types.invoice_currency_amount

        out["BaseCurrencyAmount"] = (
            aws_sdk_invoicing.types.invoice_currency_amount.serialize_aws_json_1_0(
                value["base_currency_amount"]
            )
        )
    if "tax_currency_amount" in value:
        import aws_sdk_invoicing.types.invoice_currency_amount

        out["TaxCurrencyAmount"] = (
            aws_sdk_invoicing.types.invoice_currency_amount.serialize_aws_json_1_0(
                value["tax_currency_amount"]
            )
        )
    if "payment_currency_amount" in value:
        import aws_sdk_invoicing.types.invoice_currency_amount

        out["PaymentCurrencyAmount"] = (
            aws_sdk_invoicing.types.invoice_currency_amount.serialize_aws_json_1_0(
                value["payment_currency_amount"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InvoiceSummary:
    out: InvoiceSummary = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "InvoiceId" in data:
        out["invoice_id"] = data["InvoiceId"]
    if "IssuedDate" in data:
        import aws_sdk_invoicing.types._prelude.timestamp

        out["issued_date"] = (
            aws_sdk_invoicing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["IssuedDate"]
            )
        )
    if "DueDate" in data:
        import aws_sdk_invoicing.types._prelude.timestamp

        out["due_date"] = (
            aws_sdk_invoicing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["DueDate"]
            )
        )
    if "BillSourceAccounts" in data:
        import aws_sdk_invoicing.types.bill_source_account_list

        out["bill_source_accounts"] = (
            aws_sdk_invoicing.types.bill_source_account_list.deserialize_aws_json_1_0(
                data["BillSourceAccounts"]
            )
        )
    if "BillSourceAccountsTotalCount" in data:
        out["bill_source_accounts_total_count"] = data["BillSourceAccountsTotalCount"]
    if "ReceiverRole" in data:
        import aws_sdk_invoicing.types.receiver_role

        out["receiver_role"] = (
            aws_sdk_invoicing.types.receiver_role.deserialize_aws_json_1_0(
                data["ReceiverRole"]
            )
        )
    if "Entity" in data:
        import aws_sdk_invoicing.types.entity

        out["entity"] = aws_sdk_invoicing.types.entity.deserialize_aws_json_1_0(
            data["Entity"]
        )
    if "BillingPeriod" in data:
        import aws_sdk_invoicing.types.billing_period

        out["billing_period"] = (
            aws_sdk_invoicing.types.billing_period.deserialize_aws_json_1_0(
                data["BillingPeriod"]
            )
        )
    if "InvoiceFrequency" in data:
        import aws_sdk_invoicing.types.invoice_frequency

        out["invoice_frequency"] = (
            aws_sdk_invoicing.types.invoice_frequency.deserialize_aws_json_1_0(
                data["InvoiceFrequency"]
            )
        )
    if "BillType" in data:
        import aws_sdk_invoicing.types.bill_type

        out["bill_type"] = aws_sdk_invoicing.types.bill_type.deserialize_aws_json_1_0(
            data["BillType"]
        )
    if "InvoiceType" in data:
        import aws_sdk_invoicing.types.invoice_type

        out["invoice_type"] = (
            aws_sdk_invoicing.types.invoice_type.deserialize_aws_json_1_0(
                data["InvoiceType"]
            )
        )
    if "CommercialInvoiceId" in data:
        out["commercial_invoice_id"] = data["CommercialInvoiceId"]
    if "OriginalInvoiceId" in data:
        out["original_invoice_id"] = data["OriginalInvoiceId"]
    if "PurchaseOrderNumber" in data:
        out["purchase_order_number"] = data["PurchaseOrderNumber"]
    if "EinvoiceDeliveryStatus" in data:
        import aws_sdk_invoicing.types.einvoice_delivery_status

        out["einvoice_delivery_status"] = (
            aws_sdk_invoicing.types.einvoice_delivery_status.deserialize_aws_json_1_0(
                data["EinvoiceDeliveryStatus"]
            )
        )
    if "TaxAuthorityStatus" in data:
        import aws_sdk_invoicing.types.tax_authority_status

        out["tax_authority_status"] = (
            aws_sdk_invoicing.types.tax_authority_status.deserialize_aws_json_1_0(
                data["TaxAuthorityStatus"]
            )
        )
    if "BaseCurrencyAmount" in data:
        import aws_sdk_invoicing.types.invoice_currency_amount

        out["base_currency_amount"] = (
            aws_sdk_invoicing.types.invoice_currency_amount.deserialize_aws_json_1_0(
                data["BaseCurrencyAmount"]
            )
        )
    if "TaxCurrencyAmount" in data:
        import aws_sdk_invoicing.types.invoice_currency_amount

        out["tax_currency_amount"] = (
            aws_sdk_invoicing.types.invoice_currency_amount.deserialize_aws_json_1_0(
                data["TaxCurrencyAmount"]
            )
        )
    if "PaymentCurrencyAmount" in data:
        import aws_sdk_invoicing.types.invoice_currency_amount

        out["payment_currency_amount"] = (
            aws_sdk_invoicing.types.invoice_currency_amount.deserialize_aws_json_1_0(
                data["PaymentCurrencyAmount"]
            )
        )
    return out
