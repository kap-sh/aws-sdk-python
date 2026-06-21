"""Generated from Smithy shape ``com.amazonaws.ssm#CommandInvocationStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: CommandInvocationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CommandInvocationStatus:
    return cast(CommandInvocationStatus, data)
