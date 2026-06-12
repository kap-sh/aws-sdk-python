"""Generated from Smithy shape ``com.amazonaws.iotsitewise#IdentityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

IdentityType: TypeAlias = Literal[
    "USER",
    "GROUP",
    "IAM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER",
        "GROUP",
        "IAM",
    )
)


def serialize_json(value: IdentityType) -> str:
    return value


def deserialize_json(data: str) -> IdentityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IdentityType value: {data!r}")
    return cast(IdentityType, data)
