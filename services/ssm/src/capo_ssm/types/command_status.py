"""Generated from Smithy shape ``com.amazonaws.ssm#CommandStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: CommandStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CommandStatus:
    return cast(CommandStatus, data)
