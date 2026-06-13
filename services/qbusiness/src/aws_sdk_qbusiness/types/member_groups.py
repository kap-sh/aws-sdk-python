"""Generated from Smithy shape ``com.amazonaws.qbusiness#MemberGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.member_group

MemberGroups: TypeAlias = list["aws_sdk_qbusiness.types.member_group.MemberGroup"]


# --- restJson1 ser/de ---
def serialize_json(value: MemberGroups) -> list:
    import aws_sdk_qbusiness.types.member_group

    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.member_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> MemberGroups:
    import aws_sdk_qbusiness.types.member_group

    out: MemberGroups = []
    for item in data:
        out.append(aws_sdk_qbusiness.types.member_group.deserialize_json(item))
    return out
