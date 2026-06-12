"""Generated from Smithy shape ``com.amazonaws.ssm#CommandStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

CommandStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Success",
    "Cancelled",
    "Failed",
    "TimedOut",
    "Cancelling",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "InProgress",
        "Success",
        "Cancelled",
        "Failed",
        "TimedOut",
        "Cancelling",
    )
)


def serialize_aws_json_1_1(value: CommandStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CommandStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CommandStatus value: {data!r}")
    return cast(CommandStatus, data)
