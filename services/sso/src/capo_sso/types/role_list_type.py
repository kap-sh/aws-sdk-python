"""Generated from Smithy shape ``com.amazonaws.sso#RoleListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sso.types.role_info

RoleListType: TypeAlias = list["capo_sso.types.role_info.RoleInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: RoleListType) -> list:
    import capo_sso.types.role_info

    out: list = []
    for item in value:
        out.append(capo_sso.types.role_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> RoleListType:
    import capo_sso.types.role_info

    out: RoleListType = []
    for item in data:
        out.append(capo_sso.types.role_info.deserialize_json(item))
    return out
