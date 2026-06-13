"""Generated from Smithy shape ``com.amazonaws.invoicing#ListInvoiceSummariesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_invoicing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.invoice_summaries_filter
    import aws_sdk_invoicing.types.invoice_summaries_max_results
    import aws_sdk_invoicing.types.invoice_summaries_selector
    import aws_sdk_invoicing.types.next_token_string


class ListInvoiceSummariesRequest(TypedDict):
    selector: (
        "aws_sdk_invoicing.types.invoice_summaries_selector.InvoiceSummariesSelector"
    )
    """<p>The option to retrieve details for a specific invoice by providing its unique ID. Alternatively, access information for all invoices linked to the account by providing an account ID.</p>"""
    filter: NotRequired[
        "aws_sdk_invoicing.types.invoice_summaries_filter.InvoiceSummariesFilter"
    ]
    """<p>Filters you can use to customize your invoice summary.</p>"""
    next_token: NotRequired["aws_sdk_invoicing.types.next_token_string.NextTokenString"]
    """<p>The token for the next set of results. (You received this token from a previous call.)</p>"""
    max_results: NotRequired[
        "aws_sdk_invoicing.types.invoice_summaries_max_results.InvoiceSummariesMaxResults"
    ]
    """<p>The maximum number of invoice summaries a paginated response can contain.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListInvoiceSummariesRequest) -> dict:
    out: dict = {}
    import aws_sdk_invoicing.types.invoice_summaries_selector

    out["Selector"] = (
        aws_sdk_invoicing.types.invoice_summaries_selector.serialize_aws_json_1_0(
            value["selector"]
        )
    )
    if "filter" in value:
        import aws_sdk_invoicing.types.invoice_summaries_filter

        out["Filter"] = (
            aws_sdk_invoicing.types.invoice_summaries_filter.serialize_aws_json_1_0(
                value["filter"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListInvoiceSummariesRequest:
    out: ListInvoiceSummariesRequest = {}  # type: ignore[typeddict-item]
    if "Selector" in data:
        import aws_sdk_invoicing.types.invoice_summaries_selector

        out["selector"] = (
            aws_sdk_invoicing.types.invoice_summaries_selector.deserialize_aws_json_1_0(
                data["Selector"]
            )
        )
    else:
        raise DeserializationError("ListInvoiceSummariesRequest.selector required")
    if "Filter" in data:
        import aws_sdk_invoicing.types.invoice_summaries_filter

        out["filter"] = (
            aws_sdk_invoicing.types.invoice_summaries_filter.deserialize_aws_json_1_0(
                data["Filter"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
