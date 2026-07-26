"""Generated from Smithy shape ``com.amazonaws.chime#UserErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime.types.user_error

UserErrorList: TypeAlias = list["capo_chime.types.user_error.UserError"]


# --- restJson1 ser/de ---
def serialize_json(value: UserErrorList) -> list:
    import capo_chime.types.user_error

    out: list = []
    for item in value:
        out.append(capo_chime.types.user_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserErrorList:
    import capo_chime.types.user_error

    out: UserErrorList = []
    for item in data:
        out.append(capo_chime.types.user_error.deserialize_json(item))
    return out
