"""Generated from Smithy shape ``com.amazonaws.finspace#KxDatabaseCacheConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_finspace.types.kx_database_cache_configuration

KxDatabaseCacheConfigurations: TypeAlias = list[
    "capo_finspace.types.kx_database_cache_configuration.KxDatabaseCacheConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: KxDatabaseCacheConfigurations) -> list:
    import capo_finspace.types.kx_database_cache_configuration

    out: list = []
    for item in value:
        out.append(
            capo_finspace.types.kx_database_cache_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> KxDatabaseCacheConfigurations:
    import capo_finspace.types.kx_database_cache_configuration

    out: KxDatabaseCacheConfigurations = []
    for item in data:
        out.append(
            capo_finspace.types.kx_database_cache_configuration.deserialize_json(item)
        )
    return out
