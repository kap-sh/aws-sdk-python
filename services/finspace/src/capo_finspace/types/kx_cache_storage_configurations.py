"""Generated from Smithy shape ``com.amazonaws.finspace#KxCacheStorageConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_finspace.types.kx_cache_storage_configuration

KxCacheStorageConfigurations: TypeAlias = list[
    "capo_finspace.types.kx_cache_storage_configuration.KxCacheStorageConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: KxCacheStorageConfigurations) -> list:
    import capo_finspace.types.kx_cache_storage_configuration

    out: list = []
    for item in value:
        out.append(
            capo_finspace.types.kx_cache_storage_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> KxCacheStorageConfigurations:
    import capo_finspace.types.kx_cache_storage_configuration

    out: KxCacheStorageConfigurations = []
    for item in data:
        out.append(
            capo_finspace.types.kx_cache_storage_configuration.deserialize_json(item)
        )
    return out
