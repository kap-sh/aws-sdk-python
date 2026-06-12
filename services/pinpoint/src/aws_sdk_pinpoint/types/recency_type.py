"""Generated from Smithy shape ``com.amazonaws.pinpoint#RecencyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint.errors import DeserializationError

RecencyType: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_json(value: RecencyType) -> str:
    return value


def deserialize_json(data: str) -> RecencyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecencyType value: {data!r}")
    return cast(RecencyType, data)
