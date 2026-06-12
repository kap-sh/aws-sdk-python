"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#RunCommandTargets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.run_command_target

RunCommandTargets: TypeAlias = list[
    "aws_sdk_cloudwatch_events.types.run_command_target.RunCommandTarget"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RunCommandTargets) -> list:
    import aws_sdk_cloudwatch_events.types.run_command_target

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_events.types.run_command_target.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RunCommandTargets:
    import aws_sdk_cloudwatch_events.types.run_command_target

    out: RunCommandTargets = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_events.types.run_command_target.deserialize_aws_json_1_1(
                item
            )
        )
    return out
