"""Generated from Smithy shape ``com.amazonaws.ivs#ThumbnailConfigurationStorageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs.types.thumbnail_configuration_storage

ThumbnailConfigurationStorageList: TypeAlias = list[
    "aws_sdk_ivs.types.thumbnail_configuration_storage.ThumbnailConfigurationStorage"
]


# --- restJson1 ser/de ---
def serialize_json(value: ThumbnailConfigurationStorageList) -> list:
    return list(value)


def deserialize_json(data: list) -> ThumbnailConfigurationStorageList:
    return list(data)
