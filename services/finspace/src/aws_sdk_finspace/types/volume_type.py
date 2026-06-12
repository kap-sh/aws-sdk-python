"""Generated from Smithy shape ``com.amazonaws.finspace#VolumeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace.errors import DeserializationError

VolumeType: TypeAlias = Literal["NAS_1",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("NAS_1",))


def serialize_json(value: VolumeType) -> str:
    return value


def deserialize_json(data: str) -> VolumeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VolumeType value: {data!r}")
    return cast(VolumeType, data)
