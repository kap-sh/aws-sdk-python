"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#Member``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_directory_service_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service_data.types.member_name
    import aws_sdk_directory_service_data.types.member_type
    import aws_sdk_directory_service_data.types.sid


class Member(TypedDict):
    sid: "aws_sdk_directory_service_data.types.sid.SID"
    """<p> The unique security identifier (SID) of the group member. </p>"""
    sam_account_name: "aws_sdk_directory_service_data.types.member_name.MemberName"
    """<p> The name of the group member. </p>"""
    member_type: "aws_sdk_directory_service_data.types.member_type.MemberType"
    """<p> The AD type of the member object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Member) -> dict:
    out: dict = {}
    out["SID"] = value["sid"]
    out["SAMAccountName"] = value["sam_account_name"]
    import aws_sdk_directory_service_data.types.member_type

    out["MemberType"] = aws_sdk_directory_service_data.types.member_type.serialize_json(
        value["member_type"]
    )
    return out


def deserialize_json(data: dict) -> Member:
    out: Member = {}  # type: ignore[typeddict-item]
    if "SID" in data:
        out["sid"] = data["SID"]
    else:
        raise DeserializationError("Member.sid required")
    if "SAMAccountName" in data:
        out["sam_account_name"] = data["SAMAccountName"]
    else:
        raise DeserializationError("Member.sam_account_name required")
    if "MemberType" in data:
        import aws_sdk_directory_service_data.types.member_type

        out["member_type"] = (
            aws_sdk_directory_service_data.types.member_type.deserialize_json(
                data["MemberType"]
            )
        )
    else:
        raise DeserializationError("Member.member_type required")
    return out
