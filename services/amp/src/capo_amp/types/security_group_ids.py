"""Generated from Smithy shape ``com.amazonaws.amp#SecurityGroupIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amp.types.security_group_id

SecurityGroupIds: TypeAlias = list["capo_amp.types.security_group_id.SecurityGroupId"]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroupIds) -> list:
    return list(value)


def deserialize_json(data: list) -> SecurityGroupIds:
    return list(data)
