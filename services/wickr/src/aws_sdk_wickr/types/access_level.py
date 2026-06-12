"""Generated from Smithy shape ``com.amazonaws.wickr#AccessLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wickr.errors import DeserializationError

AccessLevel: TypeAlias = Literal[
    "STANDARD",
    "PREMIUM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "PREMIUM",
    )
)


def serialize_json(value: AccessLevel) -> str:
    return value


def deserialize_json(data: str) -> AccessLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessLevel value: {data!r}")
    return cast(AccessLevel, data)
