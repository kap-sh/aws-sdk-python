"""Generated from Smithy shape ``com.amazonaws.finspace#KxSavedownStorageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace.errors import DeserializationError

KxSavedownStorageType: TypeAlias = Literal["SDS01",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SDS01",))


def serialize_json(value: KxSavedownStorageType) -> str:
    return value


def deserialize_json(data: str) -> KxSavedownStorageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KxSavedownStorageType value: {data!r}")
    return cast(KxSavedownStorageType, data)
