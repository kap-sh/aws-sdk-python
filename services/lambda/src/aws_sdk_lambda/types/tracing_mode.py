"""Generated from Smithy shape ``com.amazonaws.lambda#TracingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lambda.errors import DeserializationError

TracingMode: TypeAlias = Literal[
    "Active",
    "PassThrough",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "PassThrough",
    )
)


def serialize_json(value: TracingMode) -> str:
    return value


def deserialize_json(data: str) -> TracingMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TracingMode value: {data!r}")
    return cast(TracingMode, data)
