"""Generated from Smithy shape ``com.amazonaws.ssm#CommandFilterKey``."""

from typing import Literal, TypeAlias, cast

CommandFilterKey: TypeAlias = Literal[
    "InvokedAfter",
    "InvokedBefore",
    "Status",
    "ExecutionStage",
    "DocumentName",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommandFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CommandFilterKey:
    return cast(CommandFilterKey, data)
