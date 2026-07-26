"""Generated from Smithy shape ``com.amazonaws.rekognition#ListUsersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.pagination_token
    import capo_rekognition.types.user_list


class ListUsersResponse(TypedDict, closed=True):
    users: NotRequired["capo_rekognition.types.user_list.UserList"]
    """<p>List of UsersID associated with the specified collection.</p>"""
    next_token: NotRequired["capo_rekognition.types.pagination_token.PaginationToken"]
    """<p>A pagination token to be used with the subsequent request if the response is truncated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUsersResponse) -> dict:
    out: dict = {}
    if "users" in value:
        import capo_rekognition.types.user_list

        out["Users"] = capo_rekognition.types.user_list.serialize_aws_json_1_1(
            value["users"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUsersResponse:
    out: ListUsersResponse = {}  # type: ignore[typeddict-item]
    if "Users" in data:
        import capo_rekognition.types.user_list

        out["users"] = capo_rekognition.types.user_list.deserialize_aws_json_1_1(
            data["Users"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
