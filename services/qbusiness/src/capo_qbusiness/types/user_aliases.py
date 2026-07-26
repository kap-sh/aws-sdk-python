"""Generated from Smithy shape ``com.amazonaws.qbusiness#UserAliases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.user_alias

UserAliases: TypeAlias = list["capo_qbusiness.types.user_alias.UserAlias"]


# --- restJson1 ser/de ---
def serialize_json(value: UserAliases) -> list:
    import capo_qbusiness.types.user_alias

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.user_alias.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserAliases:
    import capo_qbusiness.types.user_alias

    out: UserAliases = []
    for item in data:
        out.append(capo_qbusiness.types.user_alias.deserialize_json(item))
    return out
