"""Generated from Smithy shape ``com.amazonaws.transfer#ListUsersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.listed_users
    import aws_sdk_transfer.types.next_token
    import aws_sdk_transfer.types.server_id


class ListUsersResponse(TypedDict):
    next_token: NotRequired["aws_sdk_transfer.types.next_token.NextToken"]
    """<p>When you can get additional results from the <code>ListUsers</code> call, a <code>NextToken</code> parameter is returned in the output. You can then pass in a subsequent command to the <code>NextToken</code> parameter to continue listing additional users.</p>"""
    server_id: "aws_sdk_transfer.types.server_id.ServerId"
    """<p>A system-assigned unique identifier for a server that the users are assigned to.</p>"""
    users: "aws_sdk_transfer.types.listed_users.ListedUsers"
    """<p>Returns the Transfer Family users and their properties for the <code>ServerId</code> value that you specify.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUsersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["ServerId"] = value["server_id"]
    import aws_sdk_transfer.types.listed_users

    out["Users"] = aws_sdk_transfer.types.listed_users.serialize_aws_json_1_1(
        value["users"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUsersResponse:
    out: ListUsersResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ServerId" in data:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("ListUsersResponse.server_id required")
    if "Users" in data:
        import aws_sdk_transfer.types.listed_users

        out["users"] = aws_sdk_transfer.types.listed_users.deserialize_aws_json_1_1(
            data["Users"]
        )
    else:
        raise DeserializationError("ListUsersResponse.users required")
    return out
