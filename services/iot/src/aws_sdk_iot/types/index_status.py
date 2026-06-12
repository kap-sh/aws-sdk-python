"""Generated from Smithy shape ``com.amazonaws.iot#IndexStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

IndexStatus: TypeAlias = Literal[
    "ACTIVE",
    "BUILDING",
    "REBUILDING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "BUILDING",
        "REBUILDING",
    )
)


def serialize_json(value: IndexStatus) -> str:
    return value


def deserialize_json(data: str) -> IndexStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IndexStatus value: {data!r}")
    return cast(IndexStatus, data)
