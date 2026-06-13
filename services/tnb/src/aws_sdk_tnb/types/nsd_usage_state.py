"""Generated from Smithy shape ``com.amazonaws.tnb#NsdUsageState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_tnb.errors import DeserializationError

NsdUsageState: TypeAlias = Literal[
    "IN_USE",
    "NOT_IN_USE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_USE",
        "NOT_IN_USE",
    )
)


def serialize_json(value: NsdUsageState) -> str:
    return value


def deserialize_json(data: str) -> NsdUsageState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NsdUsageState value: {data!r}")
    return cast(NsdUsageState, data)
