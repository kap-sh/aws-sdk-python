"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#Group``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_directory_service_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service_data.types.attributes
    import aws_sdk_directory_service_data.types.distinguished_name
    import aws_sdk_directory_service_data.types.group_name
    import aws_sdk_directory_service_data.types.group_scope
    import aws_sdk_directory_service_data.types.group_type
    import aws_sdk_directory_service_data.types.sid


class Group(TypedDict):
    sid: NotRequired["aws_sdk_directory_service_data.types.sid.SID"]
    """<p> The unique security identifier (SID) of the group. </p>"""
    sam_account_name: "aws_sdk_directory_service_data.types.group_name.GroupName"
    """<p> The name of the group. </p>"""
    distinguished_name: NotRequired[
        "aws_sdk_directory_service_data.types.distinguished_name.DistinguishedName"
    ]
    r"""<p>The <a href=\"https://learn.microsoft.com/en-us/windows/win32/ad/object-names-and-identities#distinguished-name\">distinguished name</a> of the object. </p>"""
    group_type: NotRequired["aws_sdk_directory_service_data.types.group_type.GroupType"]
    r"""<p> The AD group type. For details, see <a href=\"https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#how-active-directory-security-groups-work\">Active Directory security group type</a>. </p>"""
    group_scope: NotRequired[
        "aws_sdk_directory_service_data.types.group_scope.GroupScope"
    ]
    r"""<p> The scope of the AD group. For details, see <a href=\"https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#group-scope\">Active Directory security groups</a> </p>"""
    other_attributes: NotRequired[
        "aws_sdk_directory_service_data.types.attributes.Attributes"
    ]
    """<p> An expression of one or more attributes, data types, and the values of a group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Group) -> dict:
    out: dict = {}
    if "sid" in value:
        out["SID"] = value["sid"]
    out["SAMAccountName"] = value["sam_account_name"]
    if "distinguished_name" in value:
        out["DistinguishedName"] = value["distinguished_name"]
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
    return out


def deserialize_json(data: dict) -> Group:
    out: Group = {}  # type: ignore[typeddict-item]
    if "SID" in data:
        out["sid"] = data["SID"]
    if "SAMAccountName" in data:
        out["sam_account_name"] = data["SAMAccountName"]
    else:
        raise DeserializationError("Group.sam_account_name required")
    if "DistinguishedName" in data:
        out["distinguished_name"] = data["DistinguishedName"]
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
    return out
