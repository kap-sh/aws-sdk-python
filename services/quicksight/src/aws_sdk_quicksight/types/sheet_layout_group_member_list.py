"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetLayoutGroupMemberList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.sheet_layout_group_member

SheetLayoutGroupMemberList: TypeAlias = list[
    "aws_sdk_quicksight.types.sheet_layout_group_member.SheetLayoutGroupMember"
]


# --- restJson1 ser/de ---
def serialize_json(value: SheetLayoutGroupMemberList) -> list:
    import aws_sdk_quicksight.types.sheet_layout_group_member

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.sheet_layout_group_member.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SheetLayoutGroupMemberList:
    import aws_sdk_quicksight.types.sheet_layout_group_member

    out: SheetLayoutGroupMemberList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.sheet_layout_group_member.deserialize_json(item)
        )
    return out
