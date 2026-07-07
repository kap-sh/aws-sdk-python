"""Generated from Smithy shape ``com.amazonaws.medialive#BatchScheduleActionCreateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_schedule_action


class BatchScheduleActionCreateRequest(TypedDict, closed=True):
    schedule_actions: NotRequired[
        "aws_sdk_medialive.types.__list_of_schedule_action.__listOfScheduleAction"
    ]
    """A list of schedule actions to create."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchScheduleActionCreateRequest) -> dict:
    out: dict = {}
    if "schedule_actions" in value:
        import aws_sdk_medialive.types.__list_of_schedule_action

        out["scheduleActions"] = (
            aws_sdk_medialive.types.__list_of_schedule_action.serialize_json(
                value["schedule_actions"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchScheduleActionCreateRequest:
    out: BatchScheduleActionCreateRequest = {}  # type: ignore[typeddict-item]
    if "scheduleActions" in data:
        import aws_sdk_medialive.types.__list_of_schedule_action

        out["schedule_actions"] = (
            aws_sdk_medialive.types.__list_of_schedule_action.deserialize_json(
                data["scheduleActions"]
            )
        )
    return out
