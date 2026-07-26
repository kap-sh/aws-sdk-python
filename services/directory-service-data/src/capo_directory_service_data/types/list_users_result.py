"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#ListUsersResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service_data.types.directory_id
    import capo_directory_service_data.types.next_token
    import capo_directory_service_data.types.realm
    import capo_directory_service_data.types.user_summary_list


class ListUsersResult(TypedDict, closed=True):
    directory_id: NotRequired[
        "capo_directory_service_data.types.directory_id.DirectoryId"
    ]
    """<p> The identifier (ID) of the directory that's associated with the user. </p>"""
    realm: NotRequired["capo_directory_service_data.types.realm.Realm"]
    """<p> The domain that's associated with the user. </p>"""
    users: NotRequired[
        "capo_directory_service_data.types.user_summary_list.UserSummaryList"
    ]
    """<p> The user information that the request returns. </p>"""
    next_token: NotRequired["capo_directory_service_data.types.next_token.NextToken"]
    """<p> An encoded paging token for paginated calls that can be passed back to retrieve the next page. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUsersResult) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "realm" in value:
        out["Realm"] = value["realm"]
    if "users" in value:
        import capo_directory_service_data.types.user_summary_list

        out["Users"] = (
            capo_directory_service_data.types.user_summary_list.serialize_json(
                value["users"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListUsersResult:
    out: ListUsersResult = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    if "Realm" in data:
        out["realm"] = data["Realm"]
    if "Users" in data:
        import capo_directory_service_data.types.user_summary_list

        out["users"] = (
            capo_directory_service_data.types.user_summary_list.deserialize_json(
                data["Users"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
