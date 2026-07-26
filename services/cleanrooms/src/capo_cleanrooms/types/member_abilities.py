"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MemberAbilities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.member_ability

MemberAbilities: TypeAlias = list["capo_cleanrooms.types.member_ability.MemberAbility"]


# --- restJson1 ser/de ---
def serialize_json(value: MemberAbilities) -> list:
    import capo_cleanrooms.types.member_ability

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.member_ability.serialize_json(item))
    return out


def deserialize_json(data: list) -> MemberAbilities:
    import capo_cleanrooms.types.member_ability

    out: MemberAbilities = []
    for item in data:
        out.append(capo_cleanrooms.types.member_ability.deserialize_json(item))
    return out
