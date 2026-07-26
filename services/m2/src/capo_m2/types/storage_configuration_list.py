"""Generated from Smithy shape ``com.amazonaws.m2#StorageConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_m2.types.storage_configuration

StorageConfigurationList: TypeAlias = list[
    "capo_m2.types.storage_configuration.StorageConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: StorageConfigurationList) -> list:
    import capo_m2.types.storage_configuration

    out: list = []
    for item in value:
        out.append(capo_m2.types.storage_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> StorageConfigurationList:
    import capo_m2.types.storage_configuration

    out: StorageConfigurationList = []
    for item in data:
        out.append(capo_m2.types.storage_configuration.deserialize_json(item))
    return out
