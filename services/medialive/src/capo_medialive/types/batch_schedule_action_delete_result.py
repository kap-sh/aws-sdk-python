"""Generated from Smithy shape ``com.amazonaws.medialive#BatchScheduleActionDeleteResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of_schedule_action


class BatchScheduleActionDeleteResult(TypedDict, closed=True):
    schedule_actions: NotRequired[
        "capo_medialive.types.__list_of_schedule_action.__listOfScheduleAction"
    ]
    """List of actions that have been deleted from the schedule."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchScheduleActionDeleteResult) -> dict:
    out: dict = {}
    if "schedule_actions" in value:
        import capo_medialive.types.__list_of_schedule_action

        out["scheduleActions"] = (
            capo_medialive.types.__list_of_schedule_action.serialize_json(
                value["schedule_actions"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchScheduleActionDeleteResult:
    out: BatchScheduleActionDeleteResult = {}  # type: ignore[typeddict-item]
    if "scheduleActions" in data:
        import capo_medialive.types.__list_of_schedule_action

        out["schedule_actions"] = (
            capo_medialive.types.__list_of_schedule_action.deserialize_json(
                data["scheduleActions"]
            )
        )
    return out
