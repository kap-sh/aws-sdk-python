"""Generated from Smithy shape ``com.amazonaws.drs#ListStagingAccountsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_drs.types.pagination_token


class ListStagingAccountsRequest(TypedDict):
    max_results: NotRequired["int"]
    """<p>The maximum number of staging Accounts to retrieve.</p>"""
    next_token: NotRequired["aws_sdk_drs.types.pagination_token.PaginationToken"]
    """<p>The token of the next staging Account to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStagingAccountsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListStagingAccountsRequest:
    out: ListStagingAccountsRequest = {}  # type: ignore[typeddict-item]
    return out
