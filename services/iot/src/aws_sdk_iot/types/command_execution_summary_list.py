"""Generated from Smithy shape ``com.amazonaws.iot#CommandExecutionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.command_execution_summary

CommandExecutionSummaryList: TypeAlias = list[
    "aws_sdk_iot.types.command_execution_summary.CommandExecutionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CommandExecutionSummaryList) -> list:
    import aws_sdk_iot.types.command_execution_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.command_execution_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CommandExecutionSummaryList:
    import aws_sdk_iot.types.command_execution_summary

    out: CommandExecutionSummaryList = []
    for item in data:
        out.append(aws_sdk_iot.types.command_execution_summary.deserialize_json(item))
    return out
