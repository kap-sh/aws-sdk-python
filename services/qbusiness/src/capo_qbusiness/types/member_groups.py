"""Generated from Smithy shape ``com.amazonaws.qbusiness#MemberGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.member_group

MemberGroups: TypeAlias = list["capo_qbusiness.types.member_group.MemberGroup"]


# --- restJson1 ser/de ---
def serialize_json(value: MemberGroups) -> list:
    import capo_qbusiness.types.member_group

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.member_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> MemberGroups:
    import capo_qbusiness.types.member_group

    out: MemberGroups = []
    for item in data:
        out.append(capo_qbusiness.types.member_group.deserialize_json(item))
    return out
