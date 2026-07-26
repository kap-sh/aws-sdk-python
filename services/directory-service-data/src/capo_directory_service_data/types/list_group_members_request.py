"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#ListGroupMembersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_directory_service_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service_data.types.directory_id
    import capo_directory_service_data.types.group_name
    import capo_directory_service_data.types.max_results
    import capo_directory_service_data.types.next_token
    import capo_directory_service_data.types.realm


class ListGroupMembersRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service_data.types.directory_id.DirectoryId"
    """<p> The identifier (ID) of the directory that's associated with the group. </p>"""
    realm: NotRequired["capo_directory_service_data.types.realm.Realm"]
    """<p> The domain name that's associated with the group. </p> <note> <p> This parameter is optional, so you can return members from a group outside of your Managed Microsoft AD domain. When no value is defined, only members of your Managed Microsoft AD groups are returned. </p> <p> This value is case insensitive. </p> </note>"""
    member_realm: NotRequired["capo_directory_service_data.types.realm.Realm"]
    """<p> The domain name that's associated with the group member. This parameter defaults to the Managed Microsoft AD domain. </p> <note> <p> This parameter is optional and case insensitive. </p> </note>"""
    sam_account_name: "capo_directory_service_data.types.group_name.GroupName"
    """<p> The name of the group. </p>"""
    next_token: NotRequired["capo_directory_service_data.types.next_token.NextToken"]
    """<p>An encoded paging token for paginated calls that can be passed back to retrieve the next page.</p>"""
    max_results: NotRequired["capo_directory_service_data.types.max_results.MaxResults"]
    """<p> The maximum number of results to be returned per request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupMembersRequest) -> dict:
    out: dict = {}
    if "realm" in value:
        out["Realm"] = value["realm"]
    if "member_realm" in value:
        out["MemberRealm"] = value["member_realm"]
    out["SAMAccountName"] = value["sam_account_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListGroupMembersRequest:
    out: ListGroupMembersRequest = {}  # type: ignore[typeddict-item]
    if "Realm" in data:
        out["realm"] = data["Realm"]
    if "MemberRealm" in data:
        out["member_realm"] = data["MemberRealm"]
    if "SAMAccountName" in data:
        out["sam_account_name"] = data["SAMAccountName"]
    else:
        raise DeserializationError("ListGroupMembersRequest.sam_account_name required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
