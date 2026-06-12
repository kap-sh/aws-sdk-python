"""Generated from Smithy shape ``com.amazonaws.devicefarm#ExecutionResult``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_device_farm.errors import DeserializationError

ExecutionResult: TypeAlias = Literal[
    "PENDING",
    "PASSED",
    "WARNED",
    "FAILED",
    "SKIPPED",
    "ERRORED",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "PASSED",
        "WARNED",
        "FAILED",
        "SKIPPED",
        "ERRORED",
        "STOPPED",
    )
)


def serialize_aws_json_1_1(value: ExecutionResult) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionResult:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionResult value: {data!r}")
    return cast(ExecutionResult, data)
