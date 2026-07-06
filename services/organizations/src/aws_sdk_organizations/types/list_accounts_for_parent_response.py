"""Generated from Smithy shape ``com.amazonaws.organizations#ListAccountsForParentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_organizations.types.accounts
    import aws_sdk_organizations.types.next_token


class ListAccountsForParentResponse(TypedDict, closed=True):
    accounts: NotRequired["aws_sdk_organizations.types.accounts.Accounts"]
    """<p>A list of the accounts in the specified root or OU.</p> <important> <p>The <code>Status</code> parameter in the API response will be retired on September 9, 2026. Although both the account <code>State</code> and account <code>Status</code> parameters are currently available in the Organizations APIs (<code>DescribeAccount</code>, <code>ListAccounts</code>, <code>ListAccountsForParent</code>), we recommend that you update your scripts or other code to use the <code>State</code> parameter instead of <code>Status</code> before September 9, 2026.</p> </important>"""
    next_token: NotRequired["aws_sdk_organizations.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAccountsForParentResponse) -> dict:
    out: dict = {}
    if "accounts" in value:
        import aws_sdk_organizations.types.accounts

        out["Accounts"] = aws_sdk_organizations.types.accounts.serialize_aws_json_1_1(
            value["accounts"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAccountsForParentResponse:
    out: ListAccountsForParentResponse = {}  # type: ignore[typeddict-item]
    if "Accounts" in data:
        import aws_sdk_organizations.types.accounts

        out["accounts"] = aws_sdk_organizations.types.accounts.deserialize_aws_json_1_1(
            data["Accounts"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
