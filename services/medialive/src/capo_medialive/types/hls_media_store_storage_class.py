"""Generated from Smithy shape ``com.amazonaws.medialive#HlsMediaStoreStorageClass``."""

from typing import Literal, TypeAlias, cast

"""Hls Media Store Storage Class"""
HlsMediaStoreStorageClass: TypeAlias = Literal["TEMPORAL",]


# --- restJson1 ser/de ---
def serialize_json(value: HlsMediaStoreStorageClass) -> str:
    return value


def deserialize_json(data: str) -> HlsMediaStoreStorageClass:
    return cast(HlsMediaStoreStorageClass, data)
