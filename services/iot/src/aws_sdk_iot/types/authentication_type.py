"""Generated from Smithy shape ``com.amazonaws.iot#AuthenticationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

AuthenticationType: TypeAlias = Literal[
    "CUSTOM_AUTH_X509",
    "CUSTOM_AUTH",
    "AWS_X509",
    "AWS_SIGV4",
    "DEFAULT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOM_AUTH_X509",
        "CUSTOM_AUTH",
        "AWS_X509",
        "AWS_SIGV4",
        "DEFAULT",
    )
)


def serialize_json(value: AuthenticationType) -> str:
    return value


def deserialize_json(data: str) -> AuthenticationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthenticationType value: {data!r}")
    return cast(AuthenticationType, data)
