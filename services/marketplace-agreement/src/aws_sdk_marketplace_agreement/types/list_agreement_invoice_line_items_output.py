"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ListAgreementInvoiceLineItemsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.agreement_invoice_line_item_group_summaries
    import aws_sdk_marketplace_agreement.types.next_token


class ListAgreementInvoiceLineItemsOutput(TypedDict):
    agreement_invoice_line_item_group_summaries: NotRequired[
        "aws_sdk_marketplace_agreement.types.agreement_invoice_line_item_group_summaries.AgreementInvoiceLineItemGroupSummaries"
    ]
    """<p>A list of grouped billing data objects.</p>"""
    next_token: NotRequired["aws_sdk_marketplace_agreement.types.next_token.NextToken"]
    """<p>The token used for pagination. The field is <code>null</code> if there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAgreementInvoiceLineItemsOutput) -> dict:
    out: dict = {}
    if "agreement_invoice_line_item_group_summaries" in value:
        import aws_sdk_marketplace_agreement.types.agreement_invoice_line_item_group_summaries

        out["agreementInvoiceLineItemGroupSummaries"] = (
            aws_sdk_marketplace_agreement.types.agreement_invoice_line_item_group_summaries.serialize_aws_json_1_0(
                value["agreement_invoice_line_item_group_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAgreementInvoiceLineItemsOutput:
    out: ListAgreementInvoiceLineItemsOutput = {}  # type: ignore[typeddict-item]
    if "agreementInvoiceLineItemGroupSummaries" in data:
        import aws_sdk_marketplace_agreement.types.agreement_invoice_line_item_group_summaries

        out["agreement_invoice_line_item_group_summaries"] = (
            aws_sdk_marketplace_agreement.types.agreement_invoice_line_item_group_summaries.deserialize_aws_json_1_0(
                data["agreementInvoiceLineItemGroupSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
