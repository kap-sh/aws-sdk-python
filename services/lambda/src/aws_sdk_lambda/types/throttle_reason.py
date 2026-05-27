"""Generated from Smithy shape ``com.amazonaws.lambda#ThrottleReason``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_lambda.errors import DeserializationError

ThrottleReason: TypeAlias = Literal[
    "ConcurrentInvocationLimitExceeded",
    "FunctionInvocationRateLimitExceeded",
    "ReservedFunctionConcurrentInvocationLimitExceeded",
    "ReservedFunctionInvocationRateLimitExceeded",
    "CallerRateLimitExceeded",
    "ConcurrentSnapshotCreateLimitExceeded",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ConcurrentInvocationLimitExceeded",
        "FunctionInvocationRateLimitExceeded",
        "ReservedFunctionConcurrentInvocationLimitExceeded",
        "ReservedFunctionInvocationRateLimitExceeded",
        "CallerRateLimitExceeded",
        "ConcurrentSnapshotCreateLimitExceeded",
    )
)


def serialize_json(value: ThrottleReason) -> str:
    return value


def deserialize_json(data: str) -> ThrottleReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThrottleReason value: {data!r}")
    return cast(ThrottleReason, data)
