"""Generated from Smithy shape ``com.amazonaws.eventbridge#RunCommandTargetValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridge.types.run_command_target_value

RunCommandTargetValues: TypeAlias = list[
    "capo_eventbridge.types.run_command_target_value.RunCommandTargetValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RunCommandTargetValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RunCommandTargetValues:
    return [item for item in data if item is not None]
