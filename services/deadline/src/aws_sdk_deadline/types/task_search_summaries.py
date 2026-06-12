"""Generated from Smithy shape ``com.amazonaws.deadline#TaskSearchSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.task_search_summary

TaskSearchSummaries: TypeAlias = list[
    "aws_sdk_deadline.types.task_search_summary.TaskSearchSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskSearchSummaries) -> list:
    import aws_sdk_deadline.types.task_search_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.task_search_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> TaskSearchSummaries:
    import aws_sdk_deadline.types.task_search_summary

    out: TaskSearchSummaries = []
    for item in data:
        out.append(aws_sdk_deadline.types.task_search_summary.deserialize_json(item))
    return out
