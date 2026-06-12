"""Generated from Smithy shape ``com.amazonaws.workmail#ListUsersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.next_token
    import aws_sdk_workmail.types.users


class ListUsersResponse(TypedDict):
    users: NotRequired["aws_sdk_workmail.types.users.Users"]
    """<p>The overview of users for an organization.</p>"""
    next_token: NotRequired["aws_sdk_workmail.types.next_token.NextToken"]
    """<p> The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUsersResponse) -> dict:
    out: dict = {}
    if "users" in value:
        import aws_sdk_workmail.types.users

        out["Users"] = aws_sdk_workmail.types.users.serialize_aws_json_1_1(
            value["users"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUsersResponse:
    out: ListUsersResponse = {}  # type: ignore[typeddict-item]
    if "Users" in data:
        import aws_sdk_workmail.types.users

        out["users"] = aws_sdk_workmail.types.users.deserialize_aws_json_1_1(
            data["Users"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
