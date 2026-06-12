"""Generated from Smithy shape ``com.amazonaws.fis#AccountTargeting``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fis.errors import DeserializationError

AccountTargeting: TypeAlias = Literal[
    "single-account",
    "multi-account",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "single-account",
        "multi-account",
    )
)


def serialize_json(value: AccountTargeting) -> str:
    return value


def deserialize_json(data: str) -> AccountTargeting:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccountTargeting value: {data!r}")
    return cast(AccountTargeting, data)
