"""Generated from Smithy shape ``com.amazonaws.ivs#ThumbnailConfigurationStorageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ivs.types.thumbnail_configuration_storage

ThumbnailConfigurationStorageList: TypeAlias = list[
    "capo_ivs.types.thumbnail_configuration_storage.ThumbnailConfigurationStorage"
]


# --- restJson1 ser/de ---
def serialize_json(value: ThumbnailConfigurationStorageList) -> list:
    return list(value)


def deserialize_json(data: list) -> ThumbnailConfigurationStorageList:
    return list(data)
