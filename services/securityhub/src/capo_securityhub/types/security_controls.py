"""Generated from Smithy shape ``com.amazonaws.securityhub#SecurityControls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.security_control

SecurityControls: TypeAlias = list[
    "capo_securityhub.types.security_control.SecurityControl"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityControls) -> list:
    import capo_securityhub.types.security_control

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.security_control.serialize_json(item))
    return out


def deserialize_json(data: list) -> SecurityControls:
    import capo_securityhub.types.security_control

    out: SecurityControls = []
    for item in data:
        out.append(capo_securityhub.types.security_control.deserialize_json(item))
    return out
