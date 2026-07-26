"""Generated from Smithy shape ``com.amazonaws.finspace#KxUserList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_finspace.types.kx_user

KxUserList: TypeAlias = list["capo_finspace.types.kx_user.KxUser"]


# --- restJson1 ser/de ---
def serialize_json(value: KxUserList) -> list:
    import capo_finspace.types.kx_user

    out: list = []
    for item in value:
        out.append(capo_finspace.types.kx_user.serialize_json(item))
    return out


def deserialize_json(data: list) -> KxUserList:
    import capo_finspace.types.kx_user

    out: KxUserList = []
    for item in data:
        out.append(capo_finspace.types.kx_user.deserialize_json(item))
    return out
