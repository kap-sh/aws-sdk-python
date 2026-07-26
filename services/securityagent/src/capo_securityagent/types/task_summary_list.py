"""Generated from Smithy shape ``com.amazonaws.securityagent#TaskSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.task_summary

TaskSummaryList: TypeAlias = list["capo_securityagent.types.task_summary.TaskSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: TaskSummaryList) -> list:
    import capo_securityagent.types.task_summary

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.task_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> TaskSummaryList:
    import capo_securityagent.types.task_summary

    out: TaskSummaryList = []
    for item in data:
        out.append(capo_securityagent.types.task_summary.deserialize_json(item))
    return out
