"""Generated from Smithy shape ``com.amazonaws.medialive#ScheduleAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.schedule_action_settings
    import aws_sdk_medialive.types.schedule_action_start_settings


class ScheduleAction(TypedDict):
    action_name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The name of the action, must be unique within the schedule. This name provides the main reference to an action once it is added to the schedule. A name is unique if it is no longer in the schedule. The schedule is automatically cleaned up to remove actions with a start time of more than 1 hour ago (approximately) so at that point a name can be reused."""
    schedule_action_settings: NotRequired[
        "aws_sdk_medialive.types.schedule_action_settings.ScheduleActionSettings"
    ]
    """Settings for this schedule action."""
    schedule_action_start_settings: NotRequired[
        "aws_sdk_medialive.types.schedule_action_start_settings.ScheduleActionStartSettings"
    ]
    """The time for the action to start in the channel."""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleAction) -> dict:
    out: dict = {}
    if "action_name" in value:
        out["actionName"] = value["action_name"]
    if "schedule_action_settings" in value:
        import aws_sdk_medialive.types.schedule_action_settings

        out["scheduleActionSettings"] = (
            aws_sdk_medialive.types.schedule_action_settings.serialize_json(
                value["schedule_action_settings"]
            )
        )
    if "schedule_action_start_settings" in value:
        import aws_sdk_medialive.types.schedule_action_start_settings

        out["scheduleActionStartSettings"] = (
            aws_sdk_medialive.types.schedule_action_start_settings.serialize_json(
                value["schedule_action_start_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> ScheduleAction:
    out: ScheduleAction = {}  # type: ignore[typeddict-item]
    if "actionName" in data:
        out["action_name"] = data["actionName"]
    if "scheduleActionSettings" in data:
        import aws_sdk_medialive.types.schedule_action_settings

        out["schedule_action_settings"] = (
            aws_sdk_medialive.types.schedule_action_settings.deserialize_json(
                data["scheduleActionSettings"]
            )
        )
    if "scheduleActionStartSettings" in data:
        import aws_sdk_medialive.types.schedule_action_start_settings

        out["schedule_action_start_settings"] = (
            aws_sdk_medialive.types.schedule_action_start_settings.deserialize_json(
                data["scheduleActionStartSettings"]
            )
        )
    return out
