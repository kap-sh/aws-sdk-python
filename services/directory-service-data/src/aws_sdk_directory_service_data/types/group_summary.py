"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#GroupSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_directory_service_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service_data.types.group_name
    import aws_sdk_directory_service_data.types.group_scope
    import aws_sdk_directory_service_data.types.group_type
    import aws_sdk_directory_service_data.types.sid


class GroupSummary(TypedDict):
    sid: "aws_sdk_directory_service_data.types.sid.SID"
    """<p>The unique security identifier (SID) of the group.</p>"""
    sam_account_name: "aws_sdk_directory_service_data.types.group_name.GroupName"
    """<p>The name of the group.</p>"""
    group_type: "aws_sdk_directory_service_data.types.group_type.GroupType"
    """<p>The AD group type. For details, see <a href=\"https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#how-active-directory-security-groups-work\">Active Directory security group type</a>.</p>"""
    group_scope: "aws_sdk_directory_service_data.types.group_scope.GroupScope"
    """<p>The scope of the AD group. For details, see <a href=\"https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#group-scope\">Active Directory security groups</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupSummary) -> dict:
    out: dict = {}
    out["SID"] = value["sid"]
    out["SAMAccountName"] = value["sam_account_name"]
    import aws_sdk_directory_service_data.types.group_type

    out["GroupType"] = aws_sdk_directory_service_data.types.group_type.serialize_json(
        value["group_type"]
    )
    import aws_sdk_directory_service_data.types.group_scope

    out["GroupScope"] = aws_sdk_directory_service_data.types.group_scope.serialize_json(
        value["group_scope"]
    )
    return out


def deserialize_json(data: dict) -> GroupSummary:
    out: GroupSummary = {}  # type: ignore[typeddict-item]
    if "SID" in data:
        out["sid"] = data["SID"]
    else:
        raise DeserializationError("GroupSummary.sid required")
    if "SAMAccountName" in data:
        out["sam_account_name"] = data["SAMAccountName"]
    else:
        raise DeserializationError("GroupSummary.sam_account_name required")
    if "GroupType" in data:
        import aws_sdk_directory_service_data.types.group_type

        out["group_type"] = (
            aws_sdk_directory_service_data.types.group_type.deserialize_json(
                data["GroupType"]
            )
        )
    else:
        raise DeserializationError("GroupSummary.group_type required")
    if "GroupScope" in data:
        import aws_sdk_directory_service_data.types.group_scope

        out["group_scope"] = (
            aws_sdk_directory_service_data.types.group_scope.deserialize_json(
                data["GroupScope"]
            )
        )
    else:
        raise DeserializationError("GroupSummary.group_scope required")
    return out
