"""Generated from Smithy shape ``com.amazonaws.securityhub#SecurityControlDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.security_control_definition

SecurityControlDefinitions: TypeAlias = list[
    "capo_securityhub.types.security_control_definition.SecurityControlDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityControlDefinitions) -> list:
    import capo_securityhub.types.security_control_definition

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.security_control_definition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SecurityControlDefinitions:
    import capo_securityhub.types.security_control_definition

    out: SecurityControlDefinitions = []
    for item in data:
        out.append(
            capo_securityhub.types.security_control_definition.deserialize_json(item)
        )
    return out
