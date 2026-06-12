"""Generated from Smithy shape ``com.amazonaws.apigateway#PutMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_api_gateway.errors import DeserializationError

PutMode: TypeAlias = Literal[
    "merge",
    "overwrite",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "merge",
        "overwrite",
    )
)


def serialize_json(value: PutMode) -> str:
    return value


def deserialize_json(data: str) -> PutMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PutMode value: {data!r}")
    return cast(PutMode, data)
