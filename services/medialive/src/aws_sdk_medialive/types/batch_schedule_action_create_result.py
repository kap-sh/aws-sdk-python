"""Generated from Smithy shape ``com.amazonaws.medialive#BatchScheduleActionCreateResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_schedule_action


class BatchScheduleActionCreateResult(TypedDict):
    schedule_actions: NotRequired[
        "aws_sdk_medialive.types.__list_of_schedule_action.__listOfScheduleAction"
    ]
    """List of actions that have been created in the schedule."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchScheduleActionCreateResult) -> dict:
    out: dict = {}
    if "schedule_actions" in value:
        import aws_sdk_medialive.types.__list_of_schedule_action

        out["scheduleActions"] = (
            aws_sdk_medialive.types.__list_of_schedule_action.serialize_json(
                value["schedule_actions"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchScheduleActionCreateResult:
    out: BatchScheduleActionCreateResult = {}  # type: ignore[typeddict-item]
    if "scheduleActions" in data:
        import aws_sdk_medialive.types.__list_of_schedule_action

        out["schedule_actions"] = (
            aws_sdk_medialive.types.__list_of_schedule_action.deserialize_json(
                data["scheduleActions"]
            )
        )
    return out
