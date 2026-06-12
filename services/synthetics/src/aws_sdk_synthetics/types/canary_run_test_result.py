"""Generated from Smithy shape ``com.amazonaws.synthetics#CanaryRunTestResult``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_synthetics.errors import DeserializationError

CanaryRunTestResult: TypeAlias = Literal[
    "PASSED",
    "FAILED",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASSED",
        "FAILED",
        "UNKNOWN",
    )
)


def serialize_json(value: CanaryRunTestResult) -> str:
    return value


def deserialize_json(data: str) -> CanaryRunTestResult:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CanaryRunTestResult value: {data!r}")
    return cast(CanaryRunTestResult, data)
