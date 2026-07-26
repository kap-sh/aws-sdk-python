"""Generated from Smithy shape ``com.amazonaws.iot#SecurityProfileTargetMappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.security_profile_target_mapping

SecurityProfileTargetMappings: TypeAlias = list[
    "capo_iot.types.security_profile_target_mapping.SecurityProfileTargetMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityProfileTargetMappings) -> list:
    import capo_iot.types.security_profile_target_mapping

    out: list = []
    for item in value:
        out.append(capo_iot.types.security_profile_target_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> SecurityProfileTargetMappings:
    import capo_iot.types.security_profile_target_mapping

    out: SecurityProfileTargetMappings = []
    for item in data:
        out.append(
            capo_iot.types.security_profile_target_mapping.deserialize_json(item)
        )
    return out
