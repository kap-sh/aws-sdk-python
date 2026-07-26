"""Generated from Smithy shape ``com.amazonaws.chime#ListAccountsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.account_list
    import capo_chime.types.string


class ListAccountsResponse(TypedDict, closed=True):
    accounts: NotRequired["capo_chime.types.account_list.AccountList"]
    """<p>List of Amazon Chime accounts and account details.</p>"""
    next_token: NotRequired["capo_chime.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccountsResponse) -> dict:
    out: dict = {}
    if "accounts" in value:
        import capo_chime.types.account_list

        out["Accounts"] = capo_chime.types.account_list.serialize_json(
            value["accounts"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAccountsResponse:
    out: ListAccountsResponse = {}  # type: ignore[typeddict-item]
    if "Accounts" in data:
        import capo_chime.types.account_list

        out["accounts"] = capo_chime.types.account_list.deserialize_json(
            data["Accounts"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
