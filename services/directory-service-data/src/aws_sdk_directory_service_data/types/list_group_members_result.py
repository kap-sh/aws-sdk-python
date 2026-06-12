"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#ListGroupMembersResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service_data.types.directory_id
    import aws_sdk_directory_service_data.types.member_list
    import aws_sdk_directory_service_data.types.next_token
    import aws_sdk_directory_service_data.types.realm


class ListGroupMembersResult(TypedDict):
    directory_id: NotRequired[
        "aws_sdk_directory_service_data.types.directory_id.DirectoryId"
    ]
    """<p>Identifier (ID) of the directory associated with the group.</p>"""
    realm: NotRequired["aws_sdk_directory_service_data.types.realm.Realm"]
    """<p> The domain name that's associated with the group. </p>"""
    member_realm: NotRequired["aws_sdk_directory_service_data.types.realm.Realm"]
    """<p> The domain name that's associated with the member. </p>"""
    members: NotRequired["aws_sdk_directory_service_data.types.member_list.MemberList"]
    """<p> The member information that the request returns. </p>"""
    next_token: NotRequired["aws_sdk_directory_service_data.types.next_token.NextToken"]
    """<p> An encoded paging token for paginated calls that can be passed back to retrieve the next page. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupMembersResult) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "realm" in value:
        out["Realm"] = value["realm"]
    if "member_realm" in value:
        out["MemberRealm"] = value["member_realm"]
    if "members" in value:
        import aws_sdk_directory_service_data.types.member_list

        out["Members"] = (
            aws_sdk_directory_service_data.types.member_list.serialize_json(
                value["members"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGroupMembersResult:
    out: ListGroupMembersResult = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    if "Realm" in data:
        out["realm"] = data["Realm"]
    if "MemberRealm" in data:
        out["member_realm"] = data["MemberRealm"]
    if "Members" in data:
        import aws_sdk_directory_service_data.types.member_list

        out["members"] = (
            aws_sdk_directory_service_data.types.member_list.deserialize_json(
                data["Members"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
