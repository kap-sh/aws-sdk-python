"""Generated from Smithy shape ``com.amazonaws.connect#UserProficiencyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.user_proficiency

UserProficiencyList: TypeAlias = list[
    "capo_connect.types.user_proficiency.UserProficiency"
]


# --- restJson1 ser/de ---
def serialize_json(value: UserProficiencyList) -> list:
    import capo_connect.types.user_proficiency

    out: list = []
    for item in value:
        out.append(capo_connect.types.user_proficiency.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserProficiencyList:
    import capo_connect.types.user_proficiency

    out: UserProficiencyList = []
    for item in data:
        out.append(capo_connect.types.user_proficiency.deserialize_json(item))
    return out
