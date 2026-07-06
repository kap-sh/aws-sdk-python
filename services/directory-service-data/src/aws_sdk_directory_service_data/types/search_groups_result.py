"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#SearchGroupsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_directory_service_data.types.directory_id
    import aws_sdk_directory_service_data.types.group_list
    import aws_sdk_directory_service_data.types.next_token
    import aws_sdk_directory_service_data.types.realm


class SearchGroupsResult(TypedDict, closed=True):
    directory_id: NotRequired[
        "aws_sdk_directory_service_data.types.directory_id.DirectoryId"
    ]
    """<p> The identifier (ID) of the directory that's associated with the group. </p>"""
    realm: NotRequired["aws_sdk_directory_service_data.types.realm.Realm"]
    """<p> The domain that's associated with the group. </p>"""
    groups: NotRequired["aws_sdk_directory_service_data.types.group_list.GroupList"]
    """<p> The group information that the request returns. </p>"""
    next_token: NotRequired["aws_sdk_directory_service_data.types.next_token.NextToken"]
    """<p> An encoded paging token for paginated calls that can be passed back to retrieve the next page. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchGroupsResult) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "realm" in value:
        out["Realm"] = value["realm"]
    if "groups" in value:
        import aws_sdk_directory_service_data.types.group_list

        out["Groups"] = aws_sdk_directory_service_data.types.group_list.serialize_json(
            value["groups"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchGroupsResult:
    out: SearchGroupsResult = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    if "Realm" in data:
        out["realm"] = data["Realm"]
    if "Groups" in data:
        import aws_sdk_directory_service_data.types.group_list

        out["groups"] = (
            aws_sdk_directory_service_data.types.group_list.deserialize_json(
                data["Groups"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
