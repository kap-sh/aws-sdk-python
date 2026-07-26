"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeScheduleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of_schedule_action
    import capo_medialive.types.__string


class DescribeScheduleResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_medialive.types.__string.__string"]
    """The next token; for use in pagination."""
    schedule_actions: NotRequired[
        "capo_medialive.types.__list_of_schedule_action.__listOfScheduleAction"
    ]
    """The list of actions in the schedule."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeScheduleResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "schedule_actions" in value:
        import capo_medialive.types.__list_of_schedule_action

        out["scheduleActions"] = (
            capo_medialive.types.__list_of_schedule_action.serialize_json(
                value["schedule_actions"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeScheduleResponse:
    out: DescribeScheduleResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "scheduleActions" in data:
        import capo_medialive.types.__list_of_schedule_action

        out["schedule_actions"] = (
            capo_medialive.types.__list_of_schedule_action.deserialize_json(
                data["scheduleActions"]
            )
        )
    return out
