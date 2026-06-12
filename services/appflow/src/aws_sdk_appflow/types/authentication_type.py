"""Generated from Smithy shape ``com.amazonaws.appflow#AuthenticationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

AuthenticationType: TypeAlias = Literal[
    "OAUTH2",
    "APIKEY",
    "BASIC",
    "CUSTOM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OAUTH2",
        "APIKEY",
        "BASIC",
        "CUSTOM",
    )
)


def serialize_json(value: AuthenticationType) -> str:
    return value


def deserialize_json(data: str) -> AuthenticationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthenticationType value: {data!r}")
    return cast(AuthenticationType, data)
