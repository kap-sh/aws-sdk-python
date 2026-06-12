"""Generated from Smithy shape ``com.amazonaws.sso#ListAccountsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sso.types.account_list_type
    import aws_sdk_sso.types.next_token_type


class ListAccountsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_sso.types.next_token_type.NextTokenType"]
    """<p>The page token client that is used to retrieve the list of accounts.</p>"""
    account_list: NotRequired["aws_sdk_sso.types.account_list_type.AccountListType"]
    """<p>A paginated response with the list of account information and the next token if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccountsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "account_list" in value:
        import aws_sdk_sso.types.account_list_type

        out["accountList"] = aws_sdk_sso.types.account_list_type.serialize_json(
            value["account_list"]
        )
    return out


def deserialize_json(data: dict) -> ListAccountsResponse:
    out: ListAccountsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "accountList" in data:
        import aws_sdk_sso.types.account_list_type

        out["account_list"] = aws_sdk_sso.types.account_list_type.deserialize_json(
            data["accountList"]
        )
    return out
