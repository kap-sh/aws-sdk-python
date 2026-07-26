"""Generated from Smithy shape ``com.amazonaws.qbusiness#MemberUsers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.member_user

MemberUsers: TypeAlias = list["capo_qbusiness.types.member_user.MemberUser"]


# --- restJson1 ser/de ---
def serialize_json(value: MemberUsers) -> list:
    import capo_qbusiness.types.member_user

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.member_user.serialize_json(item))
    return out


def deserialize_json(data: list) -> MemberUsers:
    import capo_qbusiness.types.member_user

    out: MemberUsers = []
    for item in data:
        out.append(capo_qbusiness.types.member_user.deserialize_json(item))
    return out
