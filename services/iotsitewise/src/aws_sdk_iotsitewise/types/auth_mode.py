"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AuthMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

AuthMode: TypeAlias = Literal[
    "IAM",
    "SSO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IAM",
        "SSO",
    )
)


def serialize_json(value: AuthMode) -> str:
    return value


def deserialize_json(data: str) -> AuthMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthMode value: {data!r}")
    return cast(AuthMode, data)
