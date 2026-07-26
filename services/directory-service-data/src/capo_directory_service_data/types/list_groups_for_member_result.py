"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#ListGroupsForMemberResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service_data.types.directory_id
    import capo_directory_service_data.types.group_summary_list
    import capo_directory_service_data.types.next_token
    import capo_directory_service_data.types.realm


class ListGroupsForMemberResult(TypedDict, closed=True):
    directory_id: NotRequired[
        "capo_directory_service_data.types.directory_id.DirectoryId"
    ]
    """<p> The identifier (ID) of the directory that's associated with the member. </p>"""
    realm: NotRequired["capo_directory_service_data.types.realm.Realm"]
    """<p> The domain that's associated with the group. </p>"""
    member_realm: NotRequired["capo_directory_service_data.types.realm.Realm"]
    """<p> The domain that's associated with the member. </p>"""
    groups: NotRequired[
        "capo_directory_service_data.types.group_summary_list.GroupSummaryList"
    ]
    """<p> The group information that the request returns. </p>"""
    next_token: NotRequired["capo_directory_service_data.types.next_token.NextToken"]
    """<p> An encoded paging token for paginated calls that can be passed back to retrieve the next page. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupsForMemberResult) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "realm" in value:
        out["Realm"] = value["realm"]
    if "member_realm" in value:
        out["MemberRealm"] = value["member_realm"]
    if "groups" in value:
        import capo_directory_service_data.types.group_summary_list

        out["Groups"] = (
            capo_directory_service_data.types.group_summary_list.serialize_json(
                value["groups"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGroupsForMemberResult:
    out: ListGroupsForMemberResult = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    if "Realm" in data:
        out["realm"] = data["Realm"]
    if "MemberRealm" in data:
        out["member_realm"] = data["MemberRealm"]
    if "Groups" in data:
        import capo_directory_service_data.types.group_summary_list

        out["groups"] = (
            capo_directory_service_data.types.group_summary_list.deserialize_json(
                data["Groups"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
