"""Generated from Smithy shape ``com.amazonaws.securityir#IncidentResponseTeam``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.incident_responder

IncidentResponseTeam: TypeAlias = list[
    "aws_sdk_security_ir.types.incident_responder.IncidentResponder"
]


# --- restJson1 ser/de ---
def serialize_json(value: IncidentResponseTeam) -> list:
    import aws_sdk_security_ir.types.incident_responder

    out: list = []
    for item in value:
        out.append(aws_sdk_security_ir.types.incident_responder.serialize_json(item))
    return out


def deserialize_json(data: list) -> IncidentResponseTeam:
    import aws_sdk_security_ir.types.incident_responder

    out: IncidentResponseTeam = []
    for item in data:
        out.append(aws_sdk_security_ir.types.incident_responder.deserialize_json(item))
    return out
