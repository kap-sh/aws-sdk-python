"""Generated from Smithy shape ``com.amazonaws.iotsitewise#WarmTierState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

WarmTierState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: WarmTierState) -> str:
    return value


def deserialize_json(data: str) -> WarmTierState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WarmTierState value: {data!r}")
    return cast(WarmTierState, data)
