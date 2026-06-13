"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AudienceSizeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanroomsml.errors import DeserializationError

AudienceSizeType: TypeAlias = Literal[
    "ABSOLUTE",
    "PERCENTAGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ABSOLUTE",
        "PERCENTAGE",
    )
)


def serialize_json(value: AudienceSizeType) -> str:
    return value


def deserialize_json(data: str) -> AudienceSizeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AudienceSizeType value: {data!r}")
    return cast(AudienceSizeType, data)
