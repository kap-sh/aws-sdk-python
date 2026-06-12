"""Generated from Smithy shape ``com.amazonaws.mediastoredata#StorageClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediastore_data.errors import DeserializationError

StorageClass: TypeAlias = Literal["TEMPORAL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TEMPORAL",))


def serialize_json(value: StorageClass) -> str:
    return value


def deserialize_json(data: str) -> StorageClass:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StorageClass value: {data!r}")
    return cast(StorageClass, data)
