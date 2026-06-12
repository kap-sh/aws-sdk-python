"""Generated from Smithy shape ``com.amazonaws.deadline#TaskSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.task_summary

TaskSummaries: TypeAlias = list["aws_sdk_deadline.types.task_summary.TaskSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: TaskSummaries) -> list:
    import aws_sdk_deadline.types.task_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.task_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> TaskSummaries:
    import aws_sdk_deadline.types.task_summary

    out: TaskSummaries = []
    for item in data:
        out.append(aws_sdk_deadline.types.task_summary.deserialize_json(item))
    return out
