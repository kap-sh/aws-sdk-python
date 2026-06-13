"""Generated from Smithy shape ``com.amazonaws.securityagent#TaskSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.task_summary

TaskSummaryList: TypeAlias = list[
    "aws_sdk_securityagent.types.task_summary.TaskSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskSummaryList) -> list:
    import aws_sdk_securityagent.types.task_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_securityagent.types.task_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> TaskSummaryList:
    import aws_sdk_securityagent.types.task_summary

    out: TaskSummaryList = []
    for item in data:
        out.append(aws_sdk_securityagent.types.task_summary.deserialize_json(item))
    return out
