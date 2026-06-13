"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ListAgreementInvoiceLineItemsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.invoice_billing_period
    import aws_sdk_marketplace_agreement.types.invoice_type
    import aws_sdk_marketplace_agreement.types.line_item_group_by
    import aws_sdk_marketplace_agreement.types.max_results
    import aws_sdk_marketplace_agreement.types.next_token
    import aws_sdk_marketplace_agreement.types.resource_id
    import aws_sdk_marketplace_agreement.types.timestamp


class ListAgreementInvoiceLineItemsInput(TypedDict):
    agreement_id: "aws_sdk_marketplace_agreement.types.resource_id.ResourceId"
    """<p>The unique identifier of the agreement.</p>"""
    group_by: "aws_sdk_marketplace_agreement.types.line_item_group_by.LineItemGroupBy"
    """<p>Specifies a grouping strategy for line items. Currently supports <code>INVOICE_ID</code>.</p>"""
    invoice_id: NotRequired[
        "aws_sdk_marketplace_agreement.types.resource_id.ResourceId"
    ]
    """<p>An optional filter to retrieve invoice information for a specific invoice.</p>"""
    invoice_type: NotRequired[
        "aws_sdk_marketplace_agreement.types.invoice_type.InvoiceType"
    ]
    """<p>An optional filter for the type of invoice. Valid values are <code>INVOICE</code> and <code>CREDIT_MEMO</code>.</p>"""
    invoice_billing_period: NotRequired[
        "aws_sdk_marketplace_agreement.types.invoice_billing_period.InvoiceBillingPeriod"
    ]
    """<p>An optional filter for the billing period associated with the invoice.</p>"""
    before_issued_time: NotRequired[
        "aws_sdk_marketplace_agreement.types.timestamp.Timestamp"
    ]
    """<p>An optional filter for invoices issued before the specified timestamp.</p>"""
    after_issued_time: NotRequired[
        "aws_sdk_marketplace_agreement.types.timestamp.Timestamp"
    ]
    """<p>An optional filter for invoices issued after the specified timestamp.</p>"""
    max_results: NotRequired[
        "aws_sdk_marketplace_agreement.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return in the response.</p>"""
    next_token: NotRequired["aws_sdk_marketplace_agreement.types.next_token.NextToken"]
    """<p>A token to specify where to start pagination.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAgreementInvoiceLineItemsInput) -> dict:
    out: dict = {}
    out["agreementId"] = value["agreement_id"]
    import aws_sdk_marketplace_agreement.types.line_item_group_by

    out["groupBy"] = (
        aws_sdk_marketplace_agreement.types.line_item_group_by.serialize_aws_json_1_0(
            value["group_by"]
        )
    )
    if "invoice_id" in value:
        out["invoiceId"] = value["invoice_id"]
    if "invoice_type" in value:
        import aws_sdk_marketplace_agreement.types.invoice_type

        out["invoiceType"] = (
            aws_sdk_marketplace_agreement.types.invoice_type.serialize_aws_json_1_0(
                value["invoice_type"]
            )
        )
    if "invoice_billing_period" in value:
        import aws_sdk_marketplace_agreement.types.invoice_billing_period

        out["invoiceBillingPeriod"] = (
            aws_sdk_marketplace_agreement.types.invoice_billing_period.serialize_aws_json_1_0(
                value["invoice_billing_period"]
            )
        )
    if "before_issued_time" in value:
        import aws_sdk_marketplace_agreement.types.timestamp

        out["beforeIssuedTime"] = (
            aws_sdk_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["before_issued_time"]
            )
        )
    if "after_issued_time" in value:
        import aws_sdk_marketplace_agreement.types.timestamp

        out["afterIssuedTime"] = (
            aws_sdk_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["after_issued_time"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAgreementInvoiceLineItemsInput:
    out: ListAgreementInvoiceLineItemsInput = {}  # type: ignore[typeddict-item]
    if "agreementId" in data:
        out["agreement_id"] = data["agreementId"]
    else:
        raise DeserializationError(
            "ListAgreementInvoiceLineItemsInput.agreement_id required"
        )
    if "groupBy" in data:
        import aws_sdk_marketplace_agreement.types.line_item_group_by

        out["group_by"] = (
            aws_sdk_marketplace_agreement.types.line_item_group_by.deserialize_aws_json_1_0(
                data["groupBy"]
            )
        )
    else:
        raise DeserializationError(
            "ListAgreementInvoiceLineItemsInput.group_by required"
        )
    if "invoiceId" in data:
        out["invoice_id"] = data["invoiceId"]
    if "invoiceType" in data:
        import aws_sdk_marketplace_agreement.types.invoice_type

        out["invoice_type"] = (
            aws_sdk_marketplace_agreement.types.invoice_type.deserialize_aws_json_1_0(
                data["invoiceType"]
            )
        )
    if "invoiceBillingPeriod" in data:
        import aws_sdk_marketplace_agreement.types.invoice_billing_period

        out["invoice_billing_period"] = (
            aws_sdk_marketplace_agreement.types.invoice_billing_period.deserialize_aws_json_1_0(
                data["invoiceBillingPeriod"]
            )
        )
    if "beforeIssuedTime" in data:
        import aws_sdk_marketplace_agreement.types.timestamp

        out["before_issued_time"] = (
            aws_sdk_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["beforeIssuedTime"]
            )
        )
    if "afterIssuedTime" in data:
        import aws_sdk_marketplace_agreement.types.timestamp

        out["after_issued_time"] = (
            aws_sdk_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["afterIssuedTime"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
