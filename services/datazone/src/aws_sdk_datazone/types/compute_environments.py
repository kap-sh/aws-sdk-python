"""Generated from Smithy shape ``com.amazonaws.datazone#ComputeEnvironments``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

ComputeEnvironments: TypeAlias = Literal[
    "SPARK",
    "ATHENA",
    "PYTHON",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SPARK",
        "ATHENA",
        "PYTHON",
    )
)


def serialize_json(value: ComputeEnvironments) -> str:
    return value


def deserialize_json(data: str) -> ComputeEnvironments:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComputeEnvironments value: {data!r}")
    return cast(ComputeEnvironments, data)
