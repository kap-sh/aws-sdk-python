"""Generated from Smithy shape ``com.amazonaws.mediatailor#RelativePosition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediatailor.errors import DeserializationError

RelativePosition: TypeAlias = Literal[
    "BEFORE_PROGRAM",
    "AFTER_PROGRAM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BEFORE_PROGRAM",
        "AFTER_PROGRAM",
    )
)


def serialize_json(value: RelativePosition) -> str:
    return value


def deserialize_json(data: str) -> RelativePosition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RelativePosition value: {data!r}")
    return cast(RelativePosition, data)
