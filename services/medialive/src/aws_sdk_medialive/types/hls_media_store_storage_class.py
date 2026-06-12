"""Generated from Smithy shape ``com.amazonaws.medialive#HlsMediaStoreStorageClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Hls Media Store Storage Class"""
HlsMediaStoreStorageClass: TypeAlias = Literal["TEMPORAL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TEMPORAL",))


def serialize_json(value: HlsMediaStoreStorageClass) -> str:
    return value


def deserialize_json(data: str) -> HlsMediaStoreStorageClass:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsMediaStoreStorageClass value: {data!r}")
    return cast(HlsMediaStoreStorageClass, data)
