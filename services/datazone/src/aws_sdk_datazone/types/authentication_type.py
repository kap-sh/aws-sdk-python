"""Generated from Smithy shape ``com.amazonaws.datazone#AuthenticationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

AuthenticationType: TypeAlias = Literal[
    "BASIC",
    "OAUTH2",
    "CUSTOM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BASIC",
        "OAUTH2",
        "CUSTOM",
    )
)


def serialize_json(value: AuthenticationType) -> str:
    return value


def deserialize_json(data: str) -> AuthenticationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthenticationType value: {data!r}")
    return cast(AuthenticationType, data)
