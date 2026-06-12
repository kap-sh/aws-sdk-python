"""Generated from Smithy shape ``com.amazonaws.fms#ListAdminsManagingAccountResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.account_id_list
    import aws_sdk_fms.types.pagination_token


class ListAdminsManagingAccountResponse(TypedDict):
    admin_accounts: NotRequired["aws_sdk_fms.types.account_id_list.AccountIdList"]
    """<p>The list of accounts who manage member accounts within their <a>AdminScope</a>.</p>"""
    next_token: NotRequired["aws_sdk_fms.types.pagination_token.PaginationToken"]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Firewall Manager returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAdminsManagingAccountResponse) -> dict:
    out: dict = {}
    if "admin_accounts" in value:
        import aws_sdk_fms.types.account_id_list

        out["AdminAccounts"] = aws_sdk_fms.types.account_id_list.serialize_aws_json_1_1(
            value["admin_accounts"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAdminsManagingAccountResponse:
    out: ListAdminsManagingAccountResponse = {}  # type: ignore[typeddict-item]
    if "AdminAccounts" in data:
        import aws_sdk_fms.types.account_id_list

        out["admin_accounts"] = (
            aws_sdk_fms.types.account_id_list.deserialize_aws_json_1_1(
                data["AdminAccounts"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
