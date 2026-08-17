"""Generated from Smithy shape ``com.amazonaws.ssm#ScheduledWindowExecutionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.scheduled_window_execution

ScheduledWindowExecutionList: TypeAlias = list[
    "capo_ssm.types.scheduled_window_execution.ScheduledWindowExecution"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduledWindowExecutionList) -> list:
    import capo_ssm.types.scheduled_window_execution

    out: list = []
    for item in value:
        out.append(
            capo_ssm.types.scheduled_window_execution.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ScheduledWindowExecutionList:
    import capo_ssm.types.scheduled_window_execution

    out: ScheduledWindowExecutionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ssm.types.scheduled_window_execution.deserialize_aws_json_1_1(item)
        )
    return out
