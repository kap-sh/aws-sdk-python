"""Generated from Smithy shape ``com.amazonaws.emrcontainers#SecurityConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr_containers.types.security_configuration

SecurityConfigurations: TypeAlias = list[
    "capo_emr_containers.types.security_configuration.SecurityConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityConfigurations) -> list:
    import capo_emr_containers.types.security_configuration

    out: list = []
    for item in value:
        out.append(
            capo_emr_containers.types.security_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SecurityConfigurations:
    import capo_emr_containers.types.security_configuration

    out: SecurityConfigurations = []
    for item in data:
        out.append(
            capo_emr_containers.types.security_configuration.deserialize_json(item)
        )
    return out
