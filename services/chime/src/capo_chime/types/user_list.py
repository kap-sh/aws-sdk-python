"""Generated from Smithy shape ``com.amazonaws.chime#UserList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime.types.user

UserList: TypeAlias = list["capo_chime.types.user.User"]


# --- restJson1 ser/de ---
def serialize_json(value: UserList) -> list:
    import capo_chime.types.user

    out: list = []
    for item in value:
        out.append(capo_chime.types.user.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserList:
    import capo_chime.types.user

    out: UserList = []
    for item in data:
        out.append(capo_chime.types.user.deserialize_json(item))
    return out
