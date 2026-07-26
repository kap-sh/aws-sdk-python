"""Generated from Smithy shape ``com.amazonaws.connect#UserProficiencyDisassociateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.user_proficiency_disassociate

UserProficiencyDisassociateList: TypeAlias = list[
    "capo_connect.types.user_proficiency_disassociate.UserProficiencyDisassociate"
]


# --- restJson1 ser/de ---
def serialize_json(value: UserProficiencyDisassociateList) -> list:
    import capo_connect.types.user_proficiency_disassociate

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.user_proficiency_disassociate.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> UserProficiencyDisassociateList:
    import capo_connect.types.user_proficiency_disassociate

    out: UserProficiencyDisassociateList = []
    for item in data:
        out.append(
            capo_connect.types.user_proficiency_disassociate.deserialize_json(item)
        )
    return out
