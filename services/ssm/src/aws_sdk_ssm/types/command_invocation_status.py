"""Generated from Smithy shape ``com.amazonaws.ssm#CommandInvocationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

CommandInvocationStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Delayed",
    "Success",
    "Cancelled",
    "TimedOut",
    "Failed",
    "Cancelling",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "InProgress",
        "Delayed",
        "Success",
        "Cancelled",
        "TimedOut",
        "Failed",
        "Cancelling",
    )
)


def serialize_aws_json_1_1(value: CommandInvocationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CommandInvocationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CommandInvocationStatus value: {data!r}")
    return cast(CommandInvocationStatus, data)
