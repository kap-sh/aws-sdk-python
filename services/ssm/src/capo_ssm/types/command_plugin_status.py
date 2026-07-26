"""Generated from Smithy shape ``com.amazonaws.ssm#CommandPluginStatus``."""

from typing import Literal, TypeAlias, cast

CommandPluginStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Success",
    "TimedOut",
    "Cancelled",
    "Failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommandPluginStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CommandPluginStatus:
    return cast(CommandPluginStatus, data)
