"""Generated from Smithy shape ``com.amazonaws.iot#SecurityProfileIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.security_profile_identifier

SecurityProfileIdentifiers: TypeAlias = list[
    "capo_iot.types.security_profile_identifier.SecurityProfileIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityProfileIdentifiers) -> list:
    import capo_iot.types.security_profile_identifier

    out: list = []
    for item in value:
        out.append(capo_iot.types.security_profile_identifier.serialize_json(item))
    return out


def deserialize_json(data: list) -> SecurityProfileIdentifiers:
    import capo_iot.types.security_profile_identifier

    out: SecurityProfileIdentifiers = []
    for item in data:
        out.append(capo_iot.types.security_profile_identifier.deserialize_json(item))
    return out
