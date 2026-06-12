"""Generated from Smithy shape ``com.amazonaws.deadline#CpuArchitectureType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

CpuArchitectureType: TypeAlias = Literal[
    "x86_64",
    "arm64",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "x86_64",
        "arm64",
    )
)


def serialize_json(value: CpuArchitectureType) -> str:
    return value


def deserialize_json(data: str) -> CpuArchitectureType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CpuArchitectureType value: {data!r}")
    return cast(CpuArchitectureType, data)
