"""Generated from Smithy shape ``com.amazonaws.ecs#CPUArchitecture``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

CPUArchitecture: TypeAlias = Literal[
    "X86_64",
    "ARM64",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "X86_64",
        "ARM64",
    )
)


def serialize_aws_json_1_1(value: CPUArchitecture) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CPUArchitecture:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CPUArchitecture value: {data!r}")
    return cast(CPUArchitecture, data)
