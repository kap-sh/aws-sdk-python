"""Generated from Smithy shape ``com.amazonaws.securityir#ImpactedServicesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.aws_service

ImpactedServicesList: TypeAlias = list[
    "aws_sdk_security_ir.types.aws_service.AwsService"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImpactedServicesList) -> list:
    return list(value)


def deserialize_json(data: list) -> ImpactedServicesList:
    return list(data)
