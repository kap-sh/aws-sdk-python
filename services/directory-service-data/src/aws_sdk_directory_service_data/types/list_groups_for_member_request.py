"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#ListGroupsForMemberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_directory_service_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service_data.types.directory_id
    import aws_sdk_directory_service_data.types.max_results
    import aws_sdk_directory_service_data.types.member_name
    import aws_sdk_directory_service_data.types.next_token
    import aws_sdk_directory_service_data.types.realm


class ListGroupsForMemberRequest(TypedDict, closed=True):
    directory_id: "aws_sdk_directory_service_data.types.directory_id.DirectoryId"
    """<p> The identifier (ID) of the directory that's associated with the member. </p>"""
    realm: NotRequired["aws_sdk_directory_service_data.types.realm.Realm"]
    """<p> The domain name that's associated with the group. </p> <note> <p> This parameter is optional, so you can return groups outside of your Managed Microsoft AD domain. When no value is defined, only your Managed Microsoft AD groups are returned. </p> <p> This value is case insensitive and defaults to your Managed Microsoft AD domain. </p> </note>"""
    member_realm: NotRequired["aws_sdk_directory_service_data.types.realm.Realm"]
    """<p> The domain name that's associated with the group member. </p> <note> <p> This parameter is optional, so you can limit your results to the group members in a specific domain. </p> <p> This parameter is case insensitive and defaults to <code>Realm</code> </p> </note>"""
    sam_account_name: "aws_sdk_directory_service_data.types.member_name.MemberName"
    """<p> The <code>SAMAccountName</code> of the user, group, or computer that's a member of the group. </p>"""
    next_token: NotRequired["aws_sdk_directory_service_data.types.next_token.NextToken"]
    """<p> An encoded paging token for paginated calls that can be passed back to retrieve the next page. </p>"""
    max_results: NotRequired[
        "aws_sdk_directory_service_data.types.max_results.MaxResults"
    ]
    """<p> The maximum number of results to be returned per request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupsForMemberRequest) -> dict:
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


def deserialize_json(data: dict) -> ListGroupsForMemberRequest:
    out: ListGroupsForMemberRequest = {}  # type: ignore[typeddict-item]
    if "Realm" in data:
        out["realm"] = data["Realm"]
    if "MemberRealm" in data:
        out["member_realm"] = data["MemberRealm"]
    if "SAMAccountName" in data:
        out["sam_account_name"] = data["SAMAccountName"]
    else:
        raise DeserializationError(
            "ListGroupsForMemberRequest.sam_account_name required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
