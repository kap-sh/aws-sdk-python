"""Generated from Smithy shape ``com.amazonaws.detective#MemberDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_detective.types.member_detail

MemberDetailList: TypeAlias = list["aws_sdk_detective.types.member_detail.MemberDetail"]


# --- restJson1 ser/de ---
def serialize_json(value: MemberDetailList) -> list:
    import aws_sdk_detective.types.member_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_detective.types.member_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> MemberDetailList:
    import aws_sdk_detective.types.member_detail

    out: MemberDetailList = []
    for item in data:
        out.append(aws_sdk_detective.types.member_detail.deserialize_json(item))
    return out
