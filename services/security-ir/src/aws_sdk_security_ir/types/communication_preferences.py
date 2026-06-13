"""Generated from Smithy shape ``com.amazonaws.securityir#CommunicationPreferences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.communication_type

CommunicationPreferences: TypeAlias = list[
    "aws_sdk_security_ir.types.communication_type.CommunicationType"
]


# --- restJson1 ser/de ---
def serialize_json(value: CommunicationPreferences) -> list:
    import aws_sdk_security_ir.types.communication_type

    out: list = []
    for item in value:
        out.append(aws_sdk_security_ir.types.communication_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> CommunicationPreferences:
    import aws_sdk_security_ir.types.communication_type

    out: CommunicationPreferences = []
    for item in data:
        out.append(aws_sdk_security_ir.types.communication_type.deserialize_json(item))
    return out
