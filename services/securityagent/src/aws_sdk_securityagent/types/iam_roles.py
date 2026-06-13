"""Generated from Smithy shape ``com.amazonaws.securityagent#IamRoles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.service_role

IamRoles: TypeAlias = list["aws_sdk_securityagent.types.service_role.ServiceRole"]


# --- restJson1 ser/de ---
def serialize_json(value: IamRoles) -> list:
    return list(value)


def deserialize_json(data: list) -> IamRoles:
    return list(data)
