"""Generated from Smithy shape ``com.amazonaws.drs#ListStagingAccountsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_drs.types.accounts
    import aws_sdk_drs.types.pagination_token

class ListStagingAccountsResponse(TypedDict):
    accounts: NotRequired["aws_sdk_drs.types.accounts.Accounts"]
    """<p>An array of staging AWS Accounts.</p>"""
    next_token: NotRequired["aws_sdk_drs.types.pagination_token.PaginationToken"]
    """<p>The token of the next staging Account to retrieve.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ListStagingAccountsResponse) -> dict:
    out: dict = {}
    if "accounts" in value:
        import aws_sdk_drs.types.accounts
        out["accounts"] = aws_sdk_drs.types.accounts.serialize_json(value["accounts"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListStagingAccountsResponse:
    out: ListStagingAccountsResponse = {}  # type: ignore[typeddict-item]
    if "accounts" in data:
        import aws_sdk_drs.types.accounts
        out["accounts"] = aws_sdk_drs.types.accounts.deserialize_json(data["accounts"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out