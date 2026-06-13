"""Generated from Smithy shape ``com.amazonaws.backup#ScheduledRunsPreview``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.scheduled_plan_execution_member

ScheduledRunsPreview: TypeAlias = list[
    "aws_sdk_backup.types.scheduled_plan_execution_member.ScheduledPlanExecutionMember"
]


# --- restJson1 ser/de ---
def serialize_json(value: ScheduledRunsPreview) -> list:
    import aws_sdk_backup.types.scheduled_plan_execution_member

    out: list = []
    for item in value:
        out.append(
            aws_sdk_backup.types.scheduled_plan_execution_member.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ScheduledRunsPreview:
    import aws_sdk_backup.types.scheduled_plan_execution_member

    out: ScheduledRunsPreview = []
    for item in data:
        out.append(
            aws_sdk_backup.types.scheduled_plan_execution_member.deserialize_json(item)
        )
    return out
