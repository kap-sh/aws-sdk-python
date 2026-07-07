"""Generated from Smithy shape ``com.amazonaws.fms#ListMemberAccountsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fms.types.member_accounts
    import aws_sdk_fms.types.pagination_token


class ListMemberAccountsResponse(TypedDict, closed=True):
    member_accounts: NotRequired["aws_sdk_fms.types.member_accounts.MemberAccounts"]
    """<p>An array of account IDs.</p>"""
    next_token: NotRequired["aws_sdk_fms.types.pagination_token.PaginationToken"]
    """<p>If you have more member account IDs than the number that you specified for <code>MaxResults</code> in the request, the response includes a <code>NextToken</code> value. To list more IDs, submit another <code>ListMemberAccounts</code> request, and specify the <code>NextToken</code> value from the response in the <code>NextToken</code> value in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMemberAccountsResponse) -> dict:
    out: dict = {}
    if "member_accounts" in value:
        import aws_sdk_fms.types.member_accounts

        out["MemberAccounts"] = (
            aws_sdk_fms.types.member_accounts.serialize_aws_json_1_1(
                value["member_accounts"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMemberAccountsResponse:
    out: ListMemberAccountsResponse = {}  # type: ignore[typeddict-item]
    if "MemberAccounts" in data:
        import aws_sdk_fms.types.member_accounts

        out["member_accounts"] = (
            aws_sdk_fms.types.member_accounts.deserialize_aws_json_1_1(
                data["MemberAccounts"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
