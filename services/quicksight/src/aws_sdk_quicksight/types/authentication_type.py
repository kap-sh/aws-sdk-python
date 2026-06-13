"""Generated from Smithy shape ``com.amazonaws.quicksight#AuthenticationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AuthenticationType: TypeAlias = Literal[
    "PASSWORD",
    "KEYPAIR",
    "TOKEN",
    "X509",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASSWORD",
        "KEYPAIR",
        "TOKEN",
        "X509",
    )
)


def serialize_json(value: AuthenticationType) -> str:
    return value


def deserialize_json(data: str) -> AuthenticationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthenticationType value: {data!r}")
    return cast(AuthenticationType, data)
