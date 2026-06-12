"""Generated from Smithy shape ``com.amazonaws.chime#MemberErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime.types.member_error

MemberErrorList: TypeAlias = list["aws_sdk_chime.types.member_error.MemberError"]


# --- restJson1 ser/de ---
def serialize_json(value: MemberErrorList) -> list:
    import aws_sdk_chime.types.member_error

    out: list = []
    for item in value:
        out.append(aws_sdk_chime.types.member_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> MemberErrorList:
    import aws_sdk_chime.types.member_error

    out: MemberErrorList = []
    for item in data:
        out.append(aws_sdk_chime.types.member_error.deserialize_json(item))
    return out
