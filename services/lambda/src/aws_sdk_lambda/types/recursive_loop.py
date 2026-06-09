"""Generated from Smithy shape ``com.amazonaws.lambda#RecursiveLoop``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lambda.errors import DeserializationError

RecursiveLoop: TypeAlias = Literal[
    "Allow",
    "Terminate",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Allow",
        "Terminate",
    )
)


def serialize_json(value: RecursiveLoop) -> str:
    return value


def deserialize_json(data: str) -> RecursiveLoop:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecursiveLoop value: {data!r}")
    return cast(RecursiveLoop, data)
