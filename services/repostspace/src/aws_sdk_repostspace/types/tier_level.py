"""Generated from Smithy shape ``com.amazonaws.repostspace#TierLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_repostspace.errors import DeserializationError

TierLevel: TypeAlias = Literal[
    "BASIC",
    "STANDARD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BASIC",
        "STANDARD",
    )
)


def serialize_json(value: TierLevel) -> str:
    return value


def deserialize_json(data: str) -> TierLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TierLevel value: {data!r}")
    return cast(TierLevel, data)
