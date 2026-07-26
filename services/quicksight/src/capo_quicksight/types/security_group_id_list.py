"""Generated from Smithy shape ``com.amazonaws.quicksight#SecurityGroupIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.security_group_id

SecurityGroupIdList: TypeAlias = list[
    "capo_quicksight.types.security_group_id.SecurityGroupId"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroupIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> SecurityGroupIdList:
    return list(data)
