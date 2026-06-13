"""Generated from Smithy shape ``com.amazonaws.notifications#ListMemberAccountsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.member_accounts
    import aws_sdk_notifications.types.next_token


class ListMemberAccountsResponse(TypedDict):
    member_accounts: "aws_sdk_notifications.types.member_accounts.MemberAccounts"
    """<p>The list of member accounts that match the specified criteria.</p>"""
    next_token: NotRequired["aws_sdk_notifications.types.next_token.NextToken"]
    """<p>The token to use for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMemberAccountsResponse) -> dict:
    out: dict = {}
    import aws_sdk_notifications.types.member_accounts

    out["memberAccounts"] = aws_sdk_notifications.types.member_accounts.serialize_json(
        value["member_accounts"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMemberAccountsResponse:
    out: ListMemberAccountsResponse = {}  # type: ignore[typeddict-item]
    if "memberAccounts" in data:
        import aws_sdk_notifications.types.member_accounts

        out["member_accounts"] = (
            aws_sdk_notifications.types.member_accounts.deserialize_json(
                data["memberAccounts"]
            )
        )
    else:
        raise DeserializationError(
            "ListMemberAccountsResponse.member_accounts required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
