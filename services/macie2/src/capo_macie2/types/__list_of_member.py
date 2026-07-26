"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfMember``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.member

__listOfMember: TypeAlias = list["capo_macie2.types.member.Member"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMember) -> list:
    import capo_macie2.types.member

    out: list = []
    for item in value:
        out.append(capo_macie2.types.member.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfMember:
    import capo_macie2.types.member

    out: __listOfMember = []
    for item in data:
        out.append(capo_macie2.types.member.deserialize_json(item))
    return out
