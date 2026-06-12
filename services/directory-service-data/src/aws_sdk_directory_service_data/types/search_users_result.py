"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#SearchUsersResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service_data.types.directory_id
    import aws_sdk_directory_service_data.types.next_token
    import aws_sdk_directory_service_data.types.realm
    import aws_sdk_directory_service_data.types.user_list


class SearchUsersResult(TypedDict):
    directory_id: NotRequired[
        "aws_sdk_directory_service_data.types.directory_id.DirectoryId"
    ]
    """<p> The identifier (ID) of the directory where the address block is added. </p>"""
    realm: NotRequired["aws_sdk_directory_service_data.types.realm.Realm"]
    """<p> The domain that's associated with the user. </p>"""
    users: NotRequired["aws_sdk_directory_service_data.types.user_list.UserList"]
    """<p> The user information that the request returns. </p>"""
    next_token: NotRequired["aws_sdk_directory_service_data.types.next_token.NextToken"]
    """<p> An encoded paging token for paginated calls that can be passed back to retrieve the next page. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchUsersResult) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "realm" in value:
        out["Realm"] = value["realm"]
    if "users" in value:
        import aws_sdk_directory_service_data.types.user_list

        out["Users"] = aws_sdk_directory_service_data.types.user_list.serialize_json(
            value["users"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchUsersResult:
    out: SearchUsersResult = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    if "Realm" in data:
        out["realm"] = data["Realm"]
    if "Users" in data:
        import aws_sdk_directory_service_data.types.user_list

        out["users"] = aws_sdk_directory_service_data.types.user_list.deserialize_json(
            data["Users"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
