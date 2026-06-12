"""Generated from Smithy shape ``com.amazonaws.scheduler#ScheduleSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_scheduler.types.creation_date
    import aws_sdk_scheduler.types.last_modification_date
    import aws_sdk_scheduler.types.name
    import aws_sdk_scheduler.types.schedule_arn
    import aws_sdk_scheduler.types.schedule_group_name
    import aws_sdk_scheduler.types.schedule_state
    import aws_sdk_scheduler.types.target_summary


class ScheduleSummary(TypedDict):
    arn: NotRequired["aws_sdk_scheduler.types.schedule_arn.ScheduleArn"]
    """<p>The Amazon Resource Name (ARN) of the schedule.</p>"""
    name: NotRequired["aws_sdk_scheduler.types.name.Name"]
    """<p>The name of the schedule.</p>"""
    group_name: NotRequired[
        "aws_sdk_scheduler.types.schedule_group_name.ScheduleGroupName"
    ]
    """<p>The name of the schedule group associated with this schedule.</p>"""
    state: NotRequired["aws_sdk_scheduler.types.schedule_state.ScheduleState"]
    """<p>Specifies whether the schedule is enabled or disabled.</p>"""
    creation_date: NotRequired["aws_sdk_scheduler.types.creation_date.CreationDate"]
    """<p>The time at which the schedule was created.</p>"""
    last_modification_date: NotRequired[
        "aws_sdk_scheduler.types.last_modification_date.LastModificationDate"
    ]
    """<p>The time at which the schedule was last modified.</p>"""
    target: NotRequired["aws_sdk_scheduler.types.target_summary.TargetSummary"]
    """<p>The schedule's target details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "state" in value:
        out["State"] = value["state"]
    if "creation_date" in value:
        import aws_sdk_scheduler.types.creation_date

        out["CreationDate"] = aws_sdk_scheduler.types.creation_date.serialize_json(
            value["creation_date"]
        )
    if "last_modification_date" in value:
        import aws_sdk_scheduler.types.last_modification_date

        out["LastModificationDate"] = (
            aws_sdk_scheduler.types.last_modification_date.serialize_json(
                value["last_modification_date"]
            )
        )
    if "target" in value:
        import aws_sdk_scheduler.types.target_summary

        out["Target"] = aws_sdk_scheduler.types.target_summary.serialize_json(
            value["target"]
        )
    return out


def deserialize_json(data: dict) -> ScheduleSummary:
    out: ScheduleSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    if "State" in data:
        out["state"] = data["State"]
    if "CreationDate" in data:
        import aws_sdk_scheduler.types.creation_date

        out["creation_date"] = aws_sdk_scheduler.types.creation_date.deserialize_json(
            data["CreationDate"]
        )
    if "LastModificationDate" in data:
        import aws_sdk_scheduler.types.last_modification_date

        out["last_modification_date"] = (
            aws_sdk_scheduler.types.last_modification_date.deserialize_json(
                data["LastModificationDate"]
            )
        )
    if "Target" in data:
        import aws_sdk_scheduler.types.target_summary

        out["target"] = aws_sdk_scheduler.types.target_summary.deserialize_json(
            data["Target"]
        )
    return out
