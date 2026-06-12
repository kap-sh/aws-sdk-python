"""Generated from Smithy shape ``com.amazonaws.securityhub#AllowedOperators``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

AllowedOperators: TypeAlias = Literal[
    "AND",
    "OR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AND",
        "OR",
    )
)


def serialize_json(value: AllowedOperators) -> str:
    return value


def deserialize_json(data: str) -> AllowedOperators:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AllowedOperators value: {data!r}")
    return cast(AllowedOperators, data)
