"""Generated from Smithy shape ``com.amazonaws.tnb#UsageState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_tnb.errors import DeserializationError

UsageState: TypeAlias = Literal[
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


def serialize_json(value: UsageState) -> str:
    return value


def deserialize_json(data: str) -> UsageState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UsageState value: {data!r}")
    return cast(UsageState, data)
