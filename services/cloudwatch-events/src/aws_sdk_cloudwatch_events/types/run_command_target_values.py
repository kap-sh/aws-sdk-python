"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#RunCommandTargetValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.run_command_target_value

RunCommandTargetValues: TypeAlias = list[
    "aws_sdk_cloudwatch_events.types.run_command_target_value.RunCommandTargetValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RunCommandTargetValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RunCommandTargetValues:
    return list(data)
