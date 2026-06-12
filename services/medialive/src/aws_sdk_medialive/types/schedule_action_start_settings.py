"""Generated from Smithy shape ``com.amazonaws.medialive#ScheduleActionStartSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.fixed_mode_schedule_action_start_settings
    import aws_sdk_medialive.types.follow_mode_schedule_action_start_settings
    import aws_sdk_medialive.types.immediate_mode_schedule_action_start_settings


class ScheduleActionStartSettings(TypedDict):
    fixed_mode_schedule_action_start_settings: NotRequired[
        "aws_sdk_medialive.types.fixed_mode_schedule_action_start_settings.FixedModeScheduleActionStartSettings"
    ]
    """Option for specifying the start time for an action."""
    follow_mode_schedule_action_start_settings: NotRequired[
        "aws_sdk_medialive.types.follow_mode_schedule_action_start_settings.FollowModeScheduleActionStartSettings"
    ]
    """Option for specifying an action as relative to another action."""
    immediate_mode_schedule_action_start_settings: NotRequired[
        "aws_sdk_medialive.types.immediate_mode_schedule_action_start_settings.ImmediateModeScheduleActionStartSettings"
    ]
    """Option for specifying an action that should be applied immediately."""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleActionStartSettings) -> dict:
    out: dict = {}
    if "fixed_mode_schedule_action_start_settings" in value:
        import aws_sdk_medialive.types.fixed_mode_schedule_action_start_settings

        out["fixedModeScheduleActionStartSettings"] = (
            aws_sdk_medialive.types.fixed_mode_schedule_action_start_settings.serialize_json(
                value["fixed_mode_schedule_action_start_settings"]
            )
        )
    if "follow_mode_schedule_action_start_settings" in value:
        import aws_sdk_medialive.types.follow_mode_schedule_action_start_settings

        out["followModeScheduleActionStartSettings"] = (
            aws_sdk_medialive.types.follow_mode_schedule_action_start_settings.serialize_json(
                value["follow_mode_schedule_action_start_settings"]
            )
        )
    if "immediate_mode_schedule_action_start_settings" in value:
        import aws_sdk_medialive.types.immediate_mode_schedule_action_start_settings

        out["immediateModeScheduleActionStartSettings"] = (
            aws_sdk_medialive.types.immediate_mode_schedule_action_start_settings.serialize_json(
                value["immediate_mode_schedule_action_start_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> ScheduleActionStartSettings:
    out: ScheduleActionStartSettings = {}  # type: ignore[typeddict-item]
    if "fixedModeScheduleActionStartSettings" in data:
        import aws_sdk_medialive.types.fixed_mode_schedule_action_start_settings

        out["fixed_mode_schedule_action_start_settings"] = (
            aws_sdk_medialive.types.fixed_mode_schedule_action_start_settings.deserialize_json(
                data["fixedModeScheduleActionStartSettings"]
            )
        )
    if "followModeScheduleActionStartSettings" in data:
        import aws_sdk_medialive.types.follow_mode_schedule_action_start_settings

        out["follow_mode_schedule_action_start_settings"] = (
            aws_sdk_medialive.types.follow_mode_schedule_action_start_settings.deserialize_json(
                data["followModeScheduleActionStartSettings"]
            )
        )
    if "immediateModeScheduleActionStartSettings" in data:
        import aws_sdk_medialive.types.immediate_mode_schedule_action_start_settings

        out["immediate_mode_schedule_action_start_settings"] = (
            aws_sdk_medialive.types.immediate_mode_schedule_action_start_settings.deserialize_json(
                data["immediateModeScheduleActionStartSettings"]
            )
        )
    return out
