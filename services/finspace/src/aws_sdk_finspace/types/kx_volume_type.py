"""Generated from Smithy shape ``com.amazonaws.finspace#KxVolumeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace.errors import DeserializationError

KxVolumeType: TypeAlias = Literal["NAS_1",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("NAS_1",))


def serialize_json(value: KxVolumeType) -> str:
    return value


def deserialize_json(data: str) -> KxVolumeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KxVolumeType value: {data!r}")
    return cast(KxVolumeType, data)
