"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#UpdateGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_directory_service_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service_data.types.attributes
    import aws_sdk_directory_service_data.types.client_token
    import aws_sdk_directory_service_data.types.directory_id
    import aws_sdk_directory_service_data.types.group_name
    import aws_sdk_directory_service_data.types.group_scope
    import aws_sdk_directory_service_data.types.group_type
    import aws_sdk_directory_service_data.types.update_type


class UpdateGroupRequest(TypedDict, closed=True):
    directory_id: "aws_sdk_directory_service_data.types.directory_id.DirectoryId"
    """<p> The identifier (ID) of the directory that's associated with the group. </p>"""
    sam_account_name: "aws_sdk_directory_service_data.types.group_name.GroupName"
    """<p> The name of the group. </p>"""
    group_type: NotRequired["aws_sdk_directory_service_data.types.group_type.GroupType"]
    r"""<p> The AD group type. For details, see <a href=\"https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#how-active-directory-security-groups-work\">Active Directory security group type</a>. </p>"""
    group_scope: NotRequired[
        "aws_sdk_directory_service_data.types.group_scope.GroupScope"
    ]
    r"""<p> The scope of the AD group. For details, see <a href=\"https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#group-scope\">Active Directory security groups</a>. </p>"""
    other_attributes: NotRequired[
        "aws_sdk_directory_service_data.types.attributes.Attributes"
    ]
    """<p> An expression that defines one or more attributes with the data type and the value of each attribute. </p>"""
    update_type: NotRequired[
        "aws_sdk_directory_service_data.types.update_type.UpdateType"
    ]
    """<p> The type of update to be performed. If no value exists for the attribute, use <code>ADD</code>. Otherwise, use <code>REPLACE</code> to change an attribute value or <code>REMOVE</code> to clear the attribute value. </p>"""
    client_token: NotRequired[
        "aws_sdk_directory_service_data.types.client_token.ClientToken"
    ]
    """<p> A unique and case-sensitive identifier that you provide to make sure the idempotency of the request, so multiple identical calls have the same effect as one single call. </p> <p> A client token is valid for 8 hours after the first request that uses it completes. After 8 hours, any request with the same client token is treated as a new request. If the request succeeds, any future uses of that token will be idempotent for another 8 hours. </p> <p> If you submit a request with the same client token but change one of the other parameters within the 8-hour idempotency window, Directory Service Data returns an <code>ConflictException</code>. </p> <note> <p> This parameter is optional when using the CLI or SDK. </p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGroupRequest) -> dict:
    out: dict = {}
    out["SAMAccountName"] = value["sam_account_name"]
    if "group_type" in value:
        import aws_sdk_directory_service_data.types.group_type

        out["GroupType"] = (
            aws_sdk_directory_service_data.types.group_type.serialize_json(
                value["group_type"]
            )
        )
    if "group_scope" in value:
        import aws_sdk_directory_service_data.types.group_scope

        out["GroupScope"] = (
            aws_sdk_directory_service_data.types.group_scope.serialize_json(
                value["group_scope"]
            )
        )
    if "other_attributes" in value:
        import aws_sdk_directory_service_data.types.attributes

        out["OtherAttributes"] = (
            aws_sdk_directory_service_data.types.attributes.serialize_json(
                value["other_attributes"]
            )
        )
    if "update_type" in value:
        import aws_sdk_directory_service_data.types.update_type

        out["UpdateType"] = (
            aws_sdk_directory_service_data.types.update_type.serialize_json(
                value["update_type"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateGroupRequest:
    out: UpdateGroupRequest = {}  # type: ignore[typeddict-item]
    if "SAMAccountName" in data:
        out["sam_account_name"] = data["SAMAccountName"]
    else:
        raise DeserializationError("UpdateGroupRequest.sam_account_name required")
    if "GroupType" in data:
        import aws_sdk_directory_service_data.types.group_type

        out["group_type"] = (
            aws_sdk_directory_service_data.types.group_type.deserialize_json(
                data["GroupType"]
            )
        )
    if "GroupScope" in data:
        import aws_sdk_directory_service_data.types.group_scope

        out["group_scope"] = (
            aws_sdk_directory_service_data.types.group_scope.deserialize_json(
                data["GroupScope"]
            )
        )
    if "OtherAttributes" in data:
        import aws_sdk_directory_service_data.types.attributes

        out["other_attributes"] = (
            aws_sdk_directory_service_data.types.attributes.deserialize_json(
                data["OtherAttributes"]
            )
        )
    if "UpdateType" in data:
        import aws_sdk_directory_service_data.types.update_type

        out["update_type"] = (
            aws_sdk_directory_service_data.types.update_type.deserialize_json(
                data["UpdateType"]
            )
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
