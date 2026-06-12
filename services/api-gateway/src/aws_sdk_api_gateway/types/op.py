"""Generated from Smithy shape ``com.amazonaws.apigateway#Op``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_api_gateway.errors import DeserializationError

Op: TypeAlias = Literal[
    "add",
    "remove",
    "replace",
    "move",
    "copy",
    "test",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "add",
        "remove",
        "replace",
        "move",
        "copy",
        "test",
    )
)


def serialize_json(value: Op) -> str:
    return value


def deserialize_json(data: str) -> Op:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Op value: {data!r}")
    return cast(Op, data)
