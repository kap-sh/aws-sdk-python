"""Generated from Smithy shape ``com.amazonaws.efs#SecurityGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_efs.types.security_group

SecurityGroups: TypeAlias = list["aws_sdk_efs.types.security_group.SecurityGroup"]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroups) -> list:
    return list(value)


def deserialize_json(data: list) -> SecurityGroups:
    return list(data)
