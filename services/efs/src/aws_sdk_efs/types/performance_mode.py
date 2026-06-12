"""Generated from Smithy shape ``com.amazonaws.efs#PerformanceMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_efs.errors import DeserializationError

PerformanceMode: TypeAlias = Literal[
    "generalPurpose",
    "maxIO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "generalPurpose",
        "maxIO",
    )
)


def serialize_json(value: PerformanceMode) -> str:
    return value


def deserialize_json(data: str) -> PerformanceMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PerformanceMode value: {data!r}")
    return cast(PerformanceMode, data)
