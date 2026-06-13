"""Generated from Smithy shape ``com.amazonaws.inspector2#ListDelegatedAdminAccountsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.delegated_admin_account_list
    import aws_sdk_inspector2.types.next_token


class ListDelegatedAdminAccountsResponse(TypedDict):
    delegated_admin_accounts: NotRequired[
        "aws_sdk_inspector2.types.delegated_admin_account_list.DelegatedAdminAccountList"
    ]
    """<p>Details of the Amazon Inspector delegated administrator of your organization.</p>"""
    next_token: NotRequired["aws_sdk_inspector2.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the <code>NextToken</code> value returned from the previous request to continue listing results after the first page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDelegatedAdminAccountsResponse) -> dict:
    out: dict = {}
    if "delegated_admin_accounts" in value:
        import aws_sdk_inspector2.types.delegated_admin_account_list

        out["delegatedAdminAccounts"] = (
            aws_sdk_inspector2.types.delegated_admin_account_list.serialize_json(
                value["delegated_admin_accounts"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDelegatedAdminAccountsResponse:
    out: ListDelegatedAdminAccountsResponse = {}  # type: ignore[typeddict-item]
    if "delegatedAdminAccounts" in data:
        import aws_sdk_inspector2.types.delegated_admin_account_list

        out["delegated_admin_accounts"] = (
            aws_sdk_inspector2.types.delegated_admin_account_list.deserialize_json(
                data["delegatedAdminAccounts"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
