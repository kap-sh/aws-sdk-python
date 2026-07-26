"""Generated from Smithy shape ``com.amazonaws.chime#MemberErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime.types.member_error

MemberErrorList: TypeAlias = list["capo_chime.types.member_error.MemberError"]


# --- restJson1 ser/de ---
def serialize_json(value: MemberErrorList) -> list:
    import capo_chime.types.member_error

    out: list = []
    for item in value:
        out.append(capo_chime.types.member_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> MemberErrorList:
    import capo_chime.types.member_error

    out: MemberErrorList = []
    for item in data:
        out.append(capo_chime.types.member_error.deserialize_json(item))
    return out
