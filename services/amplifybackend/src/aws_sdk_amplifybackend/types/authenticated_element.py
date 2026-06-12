"""Generated from Smithy shape ``com.amazonaws.amplifybackend#AuthenticatedElement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplifybackend.errors import DeserializationError

AuthenticatedElement: TypeAlias = Literal[
    "READ",
    "CREATE_AND_UPDATE",
    "DELETE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READ",
        "CREATE_AND_UPDATE",
        "DELETE",
    )
)


def serialize_json(value: AuthenticatedElement) -> str:
    return value


def deserialize_json(data: str) -> AuthenticatedElement:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthenticatedElement value: {data!r}")
    return cast(AuthenticatedElement, data)
