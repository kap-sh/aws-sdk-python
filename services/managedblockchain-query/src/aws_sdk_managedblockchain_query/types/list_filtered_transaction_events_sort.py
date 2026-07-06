"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#ListFilteredTransactionEventsSort``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_managedblockchain_query.types.list_filtered_transaction_events_sort_by
    import aws_sdk_managedblockchain_query.types.sort_order


class ListFilteredTransactionEventsSort(TypedDict, closed=True):
    sort_by: NotRequired[
        "aws_sdk_managedblockchain_query.types.list_filtered_transaction_events_sort_by.ListFilteredTransactionEventsSortBy"
    ]
    """<p>Container on how the results will be sorted by?</p>"""
    sort_order: NotRequired[
        "aws_sdk_managedblockchain_query.types.sort_order.SortOrder"
    ]
    """<p>The container for the <i>sort order</i> for <code>ListFilteredTransactionEvents</code>. The <code>SortOrder</code> field only accepts the values <code>ASCENDING</code> and <code>DESCENDING</code>. Not providing <code>SortOrder</code> will default to <code>ASCENDING</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFilteredTransactionEventsSort) -> dict:
    out: dict = {}
    if "sort_by" in value:
        out["sortBy"] = value["sort_by"]
    if "sort_order" in value:
        out["sortOrder"] = value["sort_order"]
    return out


def deserialize_json(data: dict) -> ListFilteredTransactionEventsSort:
    out: ListFilteredTransactionEventsSort = {}  # type: ignore[typeddict-item]
    if "sortBy" in data:
        out["sort_by"] = data["sortBy"]
    if "sortOrder" in data:
        out["sort_order"] = data["sortOrder"]
    return out
