"""Generated from Smithy shape ``com.amazonaws.athena#ExecutorState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_athena.errors import DeserializationError

ExecutorState: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "REGISTERED",
    "TERMINATING",
    "TERMINATED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATED",
        "REGISTERED",
        "TERMINATING",
        "TERMINATED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: ExecutorState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutorState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutorState value: {data!r}")
    return cast(ExecutorState, data)
