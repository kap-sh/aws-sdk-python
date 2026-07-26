"""Generated from Smithy shape ``com.amazonaws.drs#ListStagingAccountsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.pagination_token


class ListStagingAccountsRequest(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of staging Accounts to retrieve.</p>"""
    next_token: NotRequired["capo_drs.types.pagination_token.PaginationToken"]
    """<p>The token of the next staging Account to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStagingAccountsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListStagingAccountsRequest:
    out: ListStagingAccountsRequest = {}  # type: ignore[typeddict-item]
    return out
