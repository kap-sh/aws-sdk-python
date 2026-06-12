"""Generated from Smithy shape ``com.amazonaws.finspace#KxCacheStorageConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_cache_storage_configuration

KxCacheStorageConfigurations: TypeAlias = list[
    "aws_sdk_finspace.types.kx_cache_storage_configuration.KxCacheStorageConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: KxCacheStorageConfigurations) -> list:
    import aws_sdk_finspace.types.kx_cache_storage_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_finspace.types.kx_cache_storage_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> KxCacheStorageConfigurations:
    import aws_sdk_finspace.types.kx_cache_storage_configuration

    out: KxCacheStorageConfigurations = []
    for item in data:
        out.append(
            aws_sdk_finspace.types.kx_cache_storage_configuration.deserialize_json(item)
        )
    return out
