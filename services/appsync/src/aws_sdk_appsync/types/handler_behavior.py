"""Generated from Smithy shape ``com.amazonaws.appsync#HandlerBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

HandlerBehavior: TypeAlias = Literal[
    "CODE",
    "DIRECT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CODE",
        "DIRECT",
    )
)


def serialize_json(value: HandlerBehavior) -> str:
    return value


def deserialize_json(data: str) -> HandlerBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HandlerBehavior value: {data!r}")
    return cast(HandlerBehavior, data)
