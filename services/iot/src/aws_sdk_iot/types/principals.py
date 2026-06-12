"""Generated from Smithy shape ``com.amazonaws.iot#Principals``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.principal_arn

Principals: TypeAlias = list["aws_sdk_iot.types.principal_arn.PrincipalArn"]


# --- restJson1 ser/de ---
def serialize_json(value: Principals) -> list:
    return list(value)


def deserialize_json(data: list) -> Principals:
    return list(data)
