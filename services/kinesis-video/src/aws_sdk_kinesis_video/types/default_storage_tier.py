"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#DefaultStorageTier``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video.errors import DeserializationError

DefaultStorageTier: TypeAlias = Literal[
    "HOT",
    "WARM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HOT",
        "WARM",
    )
)


def serialize_json(value: DefaultStorageTier) -> str:
    return value


def deserialize_json(data: str) -> DefaultStorageTier:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DefaultStorageTier value: {data!r}")
    return cast(DefaultStorageTier, data)
