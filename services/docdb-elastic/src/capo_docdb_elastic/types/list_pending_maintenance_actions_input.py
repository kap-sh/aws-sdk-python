"""Generated from Smithy shape ``com.amazonaws.docdbelastic#ListPendingMaintenanceActionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_docdb_elastic.types.pagination_token


class ListPendingMaintenanceActionsInput(TypedDict, closed=True):
    next_token: NotRequired["capo_docdb_elastic.types.pagination_token.PaginationToken"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>maxResults</code>.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to include in the response. If more records exist than the specified <code>maxResults</code> value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPendingMaintenanceActionsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPendingMaintenanceActionsInput:
    out: ListPendingMaintenanceActionsInput = {}  # type: ignore[typeddict-item]
    return out
