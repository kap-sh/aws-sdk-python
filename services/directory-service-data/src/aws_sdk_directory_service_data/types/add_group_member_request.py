"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#AddGroupMemberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_directory_service_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service_data.types.client_token
    import aws_sdk_directory_service_data.types.directory_id
    import aws_sdk_directory_service_data.types.group_name
    import aws_sdk_directory_service_data.types.member_name
    import aws_sdk_directory_service_data.types.realm


class AddGroupMemberRequest(TypedDict, closed=True):
    directory_id: "aws_sdk_directory_service_data.types.directory_id.DirectoryId"
    """<p> The identifier (ID) of the directory that's associated with the group. </p>"""
    group_name: "aws_sdk_directory_service_data.types.group_name.GroupName"
    """<p> The name of the group. </p>"""
    member_name: "aws_sdk_directory_service_data.types.member_name.MemberName"
    """<p> The <code>SAMAccountName</code> of the user, group, or computer to add as a group member. </p>"""
    member_realm: NotRequired["aws_sdk_directory_service_data.types.realm.Realm"]
    """<p> The domain name that's associated with the group member. This parameter is required only when adding a member outside of your Managed Microsoft AD domain to a group inside of your Managed Microsoft AD domain. This parameter defaults to the Managed Microsoft AD domain. </p> <note> <p> This parameter is case insensitive. </p> </note>"""
    client_token: NotRequired[
        "aws_sdk_directory_service_data.types.client_token.ClientToken"
    ]
    """<p> A unique and case-sensitive identifier that you provide to make sure the idempotency of the request, so multiple identical calls have the same effect as one single call. </p> <p> A client token is valid for 8 hours after the first request that uses it completes. After 8 hours, any request with the same client token is treated as a new request. If the request succeeds, any future uses of that token will be idempotent for another 8 hours. </p> <p> If you submit a request with the same client token but change one of the other parameters within the 8-hour idempotency window, Directory Service Data returns an <code>ConflictException</code>. </p> <note> <p> This parameter is optional when using the CLI or SDK. </p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddGroupMemberRequest) -> dict:
    out: dict = {}
    out["GroupName"] = value["group_name"]
    out["MemberName"] = value["member_name"]
    if "member_realm" in value:
        out["MemberRealm"] = value["member_realm"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> AddGroupMemberRequest:
    out: AddGroupMemberRequest = {}  # type: ignore[typeddict-item]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    else:
        raise DeserializationError("AddGroupMemberRequest.group_name required")
    if "MemberName" in data:
        out["member_name"] = data["MemberName"]
    else:
        raise DeserializationError("AddGroupMemberRequest.member_name required")
    if "MemberRealm" in data:
        out["member_realm"] = data["MemberRealm"]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
