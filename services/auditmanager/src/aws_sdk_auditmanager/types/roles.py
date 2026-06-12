"""Generated from Smithy shape ``com.amazonaws.auditmanager#Roles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.role

Roles: TypeAlias = list["aws_sdk_auditmanager.types.role.Role"]


# --- restJson1 ser/de ---
def serialize_json(value: Roles) -> list:
    import aws_sdk_auditmanager.types.role

    out: list = []
    for item in value:
        out.append(aws_sdk_auditmanager.types.role.serialize_json(item))
    return out


def deserialize_json(data: list) -> Roles:
    import aws_sdk_auditmanager.types.role

    out: Roles = []
    for item in data:
        out.append(aws_sdk_auditmanager.types.role.deserialize_json(item))
    return out
