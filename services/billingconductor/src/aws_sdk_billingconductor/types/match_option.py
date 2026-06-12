"""Generated from Smithy shape ``com.amazonaws.billingconductor#MatchOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_billingconductor.errors import DeserializationError

MatchOption: TypeAlias = Literal[
    "NOT_EQUAL",
    "EQUAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_EQUAL",
        "EQUAL",
    )
)


def serialize_json(value: MatchOption) -> str:
    return value


def deserialize_json(data: str) -> MatchOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MatchOption value: {data!r}")
    return cast(MatchOption, data)
