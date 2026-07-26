"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ThumbnailStorageTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ivs_realtime.types.thumbnail_storage_type

ThumbnailStorageTypeList: TypeAlias = list[
    "capo_ivs_realtime.types.thumbnail_storage_type.ThumbnailStorageType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ThumbnailStorageTypeList) -> list:
    import capo_ivs_realtime.types.thumbnail_storage_type

    out: list = []
    for item in value:
        out.append(capo_ivs_realtime.types.thumbnail_storage_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThumbnailStorageTypeList:
    import capo_ivs_realtime.types.thumbnail_storage_type

    out: ThumbnailStorageTypeList = []
    for item in data:
        out.append(
            capo_ivs_realtime.types.thumbnail_storage_type.deserialize_json(item)
        )
    return out
