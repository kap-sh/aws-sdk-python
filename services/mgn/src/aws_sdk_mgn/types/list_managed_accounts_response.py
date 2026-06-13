"""Generated from Smithy shape ``com.amazonaws.mgn#ListManagedAccountsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.managed_accounts
    import aws_sdk_mgn.types.pagination_token


class ListManagedAccountsResponse(TypedDict):
    items: "aws_sdk_mgn.types.managed_accounts.ManagedAccounts"
    """<p>List managed accounts response items.</p>"""
    next_token: NotRequired["aws_sdk_mgn.types.pagination_token.PaginationToken"]
    """<p>List managed accounts response next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedAccountsResponse) -> dict:
    out: dict = {}
    import aws_sdk_mgn.types.managed_accounts

    out["items"] = aws_sdk_mgn.types.managed_accounts.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListManagedAccountsResponse:
    out: ListManagedAccountsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_mgn.types.managed_accounts

        out["items"] = aws_sdk_mgn.types.managed_accounts.deserialize_json(
            data["items"]
        )
    else:
        raise DeserializationError("ListManagedAccountsResponse.items required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
