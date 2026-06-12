"""Generated from Smithy shape ``com.amazonaws.securityhub#SecurityControlDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.security_control_definition

SecurityControlDefinitions: TypeAlias = list[
    "aws_sdk_securityhub.types.security_control_definition.SecurityControlDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityControlDefinitions) -> list:
    import aws_sdk_securityhub.types.security_control_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.security_control_definition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SecurityControlDefinitions:
    import aws_sdk_securityhub.types.security_control_definition

    out: SecurityControlDefinitions = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.security_control_definition.deserialize_json(item)
        )
    return out
