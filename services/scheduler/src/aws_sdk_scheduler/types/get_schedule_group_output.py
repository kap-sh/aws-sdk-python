"""Generated from Smithy shape ``com.amazonaws.scheduler#GetScheduleGroupOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_scheduler.types.creation_date
    import aws_sdk_scheduler.types.last_modification_date
    import aws_sdk_scheduler.types.schedule_group_arn
    import aws_sdk_scheduler.types.schedule_group_name
    import aws_sdk_scheduler.types.schedule_group_state


class GetScheduleGroupOutput(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_scheduler.types.schedule_group_arn.ScheduleGroupArn"]
    """<p>The Amazon Resource Name (ARN) of the schedule group.</p>"""
    name: NotRequired["aws_sdk_scheduler.types.schedule_group_name.ScheduleGroupName"]
    """<p>The name of the schedule group.</p>"""
    state: NotRequired[
        "aws_sdk_scheduler.types.schedule_group_state.ScheduleGroupState"
    ]
    """<p>Specifies the state of the schedule group.</p>"""
    creation_date: NotRequired["aws_sdk_scheduler.types.creation_date.CreationDate"]
    """<p>The time at which the schedule group was created.</p>"""
    last_modification_date: NotRequired[
        "aws_sdk_scheduler.types.last_modification_date.LastModificationDate"
    ]
    """<p>The time at which the schedule group was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetScheduleGroupOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
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
    return out


def deserialize_json(data: dict) -> GetScheduleGroupOutput:
    out: GetScheduleGroupOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
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
    return out
