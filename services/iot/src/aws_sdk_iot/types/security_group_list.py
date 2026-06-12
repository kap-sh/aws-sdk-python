"""Generated from Smithy shape ``com.amazonaws.iot#SecurityGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.security_group_id

SecurityGroupList: TypeAlias = list[
    "aws_sdk_iot.types.security_group_id.SecurityGroupId"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroupList) -> list:
    return list(value)


def deserialize_json(data: list) -> SecurityGroupList:
    return list(data)
