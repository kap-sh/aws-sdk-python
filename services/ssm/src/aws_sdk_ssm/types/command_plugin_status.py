"""Generated from Smithy shape ``com.amazonaws.ssm#CommandPluginStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

CommandPluginStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Success",
    "TimedOut",
    "Cancelled",
    "Failed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "InProgress",
        "Success",
        "TimedOut",
        "Cancelled",
        "Failed",
    )
)


def serialize_aws_json_1_1(value: CommandPluginStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CommandPluginStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CommandPluginStatus value: {data!r}")
    return cast(CommandPluginStatus, data)
