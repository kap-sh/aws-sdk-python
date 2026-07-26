"""Generated from Smithy shape ``com.amazonaws.iot#SecurityProfileTargets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.security_profile_target

SecurityProfileTargets: TypeAlias = list[
    "capo_iot.types.security_profile_target.SecurityProfileTarget"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityProfileTargets) -> list:
    import capo_iot.types.security_profile_target

    out: list = []
    for item in value:
        out.append(capo_iot.types.security_profile_target.serialize_json(item))
    return out


def deserialize_json(data: list) -> SecurityProfileTargets:
    import capo_iot.types.security_profile_target

    out: SecurityProfileTargets = []
    for item in data:
        out.append(capo_iot.types.security_profile_target.deserialize_json(item))
    return out
