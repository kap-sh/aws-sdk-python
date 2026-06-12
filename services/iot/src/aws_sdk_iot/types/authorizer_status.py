"""Generated from Smithy shape ``com.amazonaws.iot#AuthorizerStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

AuthorizerStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_json(value: AuthorizerStatus) -> str:
    return value


def deserialize_json(data: str) -> AuthorizerStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthorizerStatus value: {data!r}")
    return cast(AuthorizerStatus, data)
