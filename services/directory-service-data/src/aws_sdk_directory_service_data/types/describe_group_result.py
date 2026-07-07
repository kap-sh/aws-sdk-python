"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#DescribeGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_directory_service_data.types.attributes
    import aws_sdk_directory_service_data.types.directory_id
    import aws_sdk_directory_service_data.types.distinguished_name
    import aws_sdk_directory_service_data.types.group_name
    import aws_sdk_directory_service_data.types.group_scope
    import aws_sdk_directory_service_data.types.group_type
    import aws_sdk_directory_service_data.types.realm
    import aws_sdk_directory_service_data.types.sid


class DescribeGroupResult(TypedDict, closed=True):
    directory_id: NotRequired[
        "aws_sdk_directory_service_data.types.directory_id.DirectoryId"
    ]
    """<p> The identifier (ID) of the directory that's associated with the group. </p>"""
    realm: NotRequired["aws_sdk_directory_service_data.types.realm.Realm"]
    """<p> The domain name that's associated with the group. </p>"""
    sid: NotRequired["aws_sdk_directory_service_data.types.sid.SID"]
    """<p> The unique security identifier (SID) of the group. </p>"""
    sam_account_name: NotRequired[
        "aws_sdk_directory_service_data.types.group_name.GroupName"
    ]
    """<p> The name of the group. </p>"""
    distinguished_name: NotRequired[
        "aws_sdk_directory_service_data.types.distinguished_name.DistinguishedName"
    ]
    r"""<p> The <a href=\"https://learn.microsoft.com/en-us/windows/win32/ad/object-names-and-identities#distinguished-name\">distinguished name</a> of the object. </p>"""
    group_type: NotRequired["aws_sdk_directory_service_data.types.group_type.GroupType"]
    r"""<p> The AD group type. For details, see <a href=\"https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#how-active-directory-security-groups-work\">Active Directory security group type</a>. </p>"""
    group_scope: NotRequired[
        "aws_sdk_directory_service_data.types.group_scope.GroupScope"
    ]
    r"""<p> The scope of the AD group. For details, see <a href=\"https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#group-scope\">Active Directory security groups</a>. </p>"""
    other_attributes: NotRequired[
        "aws_sdk_directory_service_data.types.attributes.Attributes"
    ]
    """<p> The attribute values that are returned for the attribute names that are included in the request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeGroupResult) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "realm" in value:
        out["Realm"] = value["realm"]
    if "sid" in value:
        out["SID"] = value["sid"]
    if "sam_account_name" in value:
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


def deserialize_json(data: dict) -> DescribeGroupResult:
    out: DescribeGroupResult = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    if "Realm" in data:
        out["realm"] = data["Realm"]
    if "SID" in data:
        out["sid"] = data["SID"]
    if "SAMAccountName" in data:
        out["sam_account_name"] = data["SAMAccountName"]
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
