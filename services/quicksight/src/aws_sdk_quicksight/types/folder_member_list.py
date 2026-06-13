"""Generated from Smithy shape ``com.amazonaws.quicksight#FolderMemberList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.member_id_arn_pair

FolderMemberList: TypeAlias = list[
    "aws_sdk_quicksight.types.member_id_arn_pair.MemberIdArnPair"
]


# --- restJson1 ser/de ---
def serialize_json(value: FolderMemberList) -> list:
    import aws_sdk_quicksight.types.member_id_arn_pair

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.member_id_arn_pair.serialize_json(item))
    return out


def deserialize_json(data: list) -> FolderMemberList:
    import aws_sdk_quicksight.types.member_id_arn_pair

    out: FolderMemberList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.member_id_arn_pair.deserialize_json(item))
    return out
