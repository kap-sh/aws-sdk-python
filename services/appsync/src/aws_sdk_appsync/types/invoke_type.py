"""Generated from Smithy shape ``com.amazonaws.appsync#InvokeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

InvokeType: TypeAlias = Literal[
    "REQUEST_RESPONSE",
    "EVENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUEST_RESPONSE",
        "EVENT",
    )
)


def serialize_json(value: InvokeType) -> str:
    return value


def deserialize_json(data: str) -> InvokeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InvokeType value: {data!r}")
    return cast(InvokeType, data)
