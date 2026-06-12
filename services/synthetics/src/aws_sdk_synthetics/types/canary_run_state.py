"""Generated from Smithy shape ``com.amazonaws.synthetics#CanaryRunState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_synthetics.errors import DeserializationError

CanaryRunState: TypeAlias = Literal[
    "RUNNING",
    "PASSED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "PASSED",
        "FAILED",
    )
)


def serialize_json(value: CanaryRunState) -> str:
    return value


def deserialize_json(data: str) -> CanaryRunState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CanaryRunState value: {data!r}")
    return cast(CanaryRunState, data)
