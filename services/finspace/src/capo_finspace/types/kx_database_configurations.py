"""Generated from Smithy shape ``com.amazonaws.finspace#KxDatabaseConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_finspace.types.kx_database_configuration

KxDatabaseConfigurations: TypeAlias = list[
    "capo_finspace.types.kx_database_configuration.KxDatabaseConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: KxDatabaseConfigurations) -> list:
    import capo_finspace.types.kx_database_configuration

    out: list = []
    for item in value:
        out.append(capo_finspace.types.kx_database_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> KxDatabaseConfigurations:
    import capo_finspace.types.kx_database_configuration

    out: KxDatabaseConfigurations = []
    for item in data:
        out.append(capo_finspace.types.kx_database_configuration.deserialize_json(item))
    return out
