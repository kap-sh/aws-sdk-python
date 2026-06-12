"""Generated from Smithy shape ``com.amazonaws.swf#ExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_swf.errors import DeserializationError

ExecutionStatus: TypeAlias = Literal[
    "OPEN",
    "CLOSED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OPEN",
        "CLOSED",
    )
)


def serialize_aws_json_1_0(value: ExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionStatus value: {data!r}")
    return cast(ExecutionStatus, data)
