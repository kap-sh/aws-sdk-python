"""Generated from Smithy shape ``com.amazonaws.athena#SessionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_athena.errors import DeserializationError

SessionState: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "IDLE",
    "BUSY",
    "TERMINATING",
    "TERMINATED",
    "DEGRADED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATED",
        "IDLE",
        "BUSY",
        "TERMINATING",
        "TERMINATED",
        "DEGRADED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: SessionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SessionState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SessionState value: {data!r}")
    return cast(SessionState, data)
