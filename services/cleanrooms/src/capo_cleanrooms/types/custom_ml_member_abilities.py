"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CustomMLMemberAbilities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.custom_ml_member_ability

CustomMLMemberAbilities: TypeAlias = list[
    "capo_cleanrooms.types.custom_ml_member_ability.CustomMLMemberAbility"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomMLMemberAbilities) -> list:
    import capo_cleanrooms.types.custom_ml_member_ability

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.custom_ml_member_ability.serialize_json(item))
    return out


def deserialize_json(data: list) -> CustomMLMemberAbilities:
    import capo_cleanrooms.types.custom_ml_member_ability

    out: CustomMLMemberAbilities = []
    for item in data:
        out.append(
            capo_cleanrooms.types.custom_ml_member_ability.deserialize_json(item)
        )
    return out
