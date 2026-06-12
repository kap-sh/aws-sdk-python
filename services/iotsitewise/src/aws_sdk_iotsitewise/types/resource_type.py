"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

ResourceType: TypeAlias = Literal[
    "PORTAL",
    "PROJECT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PORTAL",
        "PROJECT",
    )
)


def serialize_json(value: ResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceType value: {data!r}")
    return cast(ResourceType, data)
