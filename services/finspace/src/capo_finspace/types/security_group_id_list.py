"""Generated from Smithy shape ``com.amazonaws.finspace#SecurityGroupIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_finspace.types.security_group_id_string

SecurityGroupIdList: TypeAlias = list[
    "capo_finspace.types.security_group_id_string.SecurityGroupIdString"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroupIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> SecurityGroupIdList:
    return list(data)
