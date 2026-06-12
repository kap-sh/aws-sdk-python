"""Generated from Smithy shape ``com.amazonaws.deadline#StepParameterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

StepParameterType: TypeAlias = Literal[
    "INT",
    "FLOAT",
    "STRING",
    "PATH",
    "CHUNK_INT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INT",
        "FLOAT",
        "STRING",
        "PATH",
        "CHUNK_INT",
    )
)


def serialize_json(value: StepParameterType) -> str:
    return value


def deserialize_json(data: str) -> StepParameterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StepParameterType value: {data!r}")
    return cast(StepParameterType, data)
