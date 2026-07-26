"""Generated from Smithy shape ``com.amazonaws.repostspace#UserAdmins``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_repostspace.types.admin_id

UserAdmins: TypeAlias = list["capo_repostspace.types.admin_id.AdminId"]


# --- restJson1 ser/de ---
def serialize_json(value: UserAdmins) -> list:
    return list(value)


def deserialize_json(data: list) -> UserAdmins:
    return list(data)
