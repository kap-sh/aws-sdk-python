"""Generated from Smithy shape ``com.amazonaws.repostspace#RoleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_repostspace.types.role

RoleList: TypeAlias = list["capo_repostspace.types.role.Role"]


# --- restJson1 ser/de ---
def serialize_json(value: RoleList) -> list:
    import capo_repostspace.types.role

    out: list = []
    for item in value:
        out.append(capo_repostspace.types.role.serialize_json(item))
    return out


def deserialize_json(data: list) -> RoleList:
    import capo_repostspace.types.role

    out: RoleList = []
    for item in data:
        out.append(capo_repostspace.types.role.deserialize_json(item))
    return out
