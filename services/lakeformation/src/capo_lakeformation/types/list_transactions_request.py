"""Generated from Smithy shape ``com.amazonaws.lakeformation#ListTransactionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.page_size
    import capo_lakeformation.types.token_string
    import capo_lakeformation.types.transaction_status_filter


class ListTransactionsRequest(TypedDict, closed=True):
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The catalog for which to list transactions. Defaults to the account ID of the caller.</p>"""
    status_filter: NotRequired[
        "capo_lakeformation.types.transaction_status_filter.TransactionStatusFilter"
    ]
    """<p> A filter indicating the status of transactions to return. Options are ALL | COMPLETED | COMMITTED | ABORTED | ACTIVE. The default is <code>ALL</code>.</p>"""
    max_results: NotRequired["capo_lakeformation.types.page_size.PageSize"]
    """<p>The maximum number of transactions to return in a single call.</p>"""
    next_token: NotRequired["capo_lakeformation.types.token_string.TokenString"]
    """<p>A continuation token if this is not the first call to retrieve transactions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTransactionsRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    if "status_filter" in value:
        import capo_lakeformation.types.transaction_status_filter

        out["StatusFilter"] = (
            capo_lakeformation.types.transaction_status_filter.serialize_json(
                value["status_filter"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTransactionsRequest:
    out: ListTransactionsRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "StatusFilter" in data:
        import capo_lakeformation.types.transaction_status_filter

        out["status_filter"] = (
            capo_lakeformation.types.transaction_status_filter.deserialize_json(
                data["StatusFilter"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
