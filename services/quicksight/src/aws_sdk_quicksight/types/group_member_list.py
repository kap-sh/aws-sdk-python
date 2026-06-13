"""Generated from Smithy shape ``com.amazonaws.quicksight#GroupMemberList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.group_member

GroupMemberList: TypeAlias = list["aws_sdk_quicksight.types.group_member.GroupMember"]


# --- restJson1 ser/de ---
def serialize_json(value: GroupMemberList) -> list:
    import aws_sdk_quicksight.types.group_member

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.group_member.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupMemberList:
    import aws_sdk_quicksight.types.group_member

    out: GroupMemberList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.group_member.deserialize_json(item))
    return out
