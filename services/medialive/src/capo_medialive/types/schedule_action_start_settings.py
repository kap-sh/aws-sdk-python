"""Generated from Smithy shape ``com.amazonaws.medialive#ScheduleActionStartSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.fixed_mode_schedule_action_start_settings
    import capo_medialive.types.follow_mode_schedule_action_start_settings
    import capo_medialive.types.immediate_mode_schedule_action_start_settings


class ScheduleActionStartSettings(TypedDict, closed=True):
    fixed_mode_schedule_action_start_settings: NotRequired[
        "capo_medialive.types.fixed_mode_schedule_action_start_settings.FixedModeScheduleActionStartSettings"
    ]
    """Option for specifying the start time for an action."""
    follow_mode_schedule_action_start_settings: NotRequired[
        "capo_medialive.types.follow_mode_schedule_action_start_settings.FollowModeScheduleActionStartSettings"
    ]
    """Option for specifying an action as relative to another action."""
    immediate_mode_schedule_action_start_settings: NotRequired[
        "capo_medialive.types.immediate_mode_schedule_action_start_settings.ImmediateModeScheduleActionStartSettings"
    ]
    """Option for specifying an action that should be applied immediately."""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleActionStartSettings) -> dict:
    out: dict = {}
    if "fixed_mode_schedule_action_start_settings" in value:
        import capo_medialive.types.fixed_mode_schedule_action_start_settings

        out["fixedModeScheduleActionStartSettings"] = (
            capo_medialive.types.fixed_mode_schedule_action_start_settings.serialize_json(
                value["fixed_mode_schedule_action_start_settings"]
            )
        )
    if "follow_mode_schedule_action_start_settings" in value:
        import capo_medialive.types.follow_mode_schedule_action_start_settings

        out["followModeScheduleActionStartSettings"] = (
            capo_medialive.types.follow_mode_schedule_action_start_settings.serialize_json(
                value["follow_mode_schedule_action_start_settings"]
            )
        )
    if "immediate_mode_schedule_action_start_settings" in value:
        import capo_medialive.types.immediate_mode_schedule_action_start_settings

        out["immediateModeScheduleActionStartSettings"] = (
            capo_medialive.types.immediate_mode_schedule_action_start_settings.serialize_json(
                value["immediate_mode_schedule_action_start_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> ScheduleActionStartSettings:
    out: ScheduleActionStartSettings = {}  # type: ignore[typeddict-item]
    if "fixedModeScheduleActionStartSettings" in data:
        import capo_medialive.types.fixed_mode_schedule_action_start_settings

        out["fixed_mode_schedule_action_start_settings"] = (
            capo_medialive.types.fixed_mode_schedule_action_start_settings.deserialize_json(
                data["fixedModeScheduleActionStartSettings"]
            )
        )
    if "followModeScheduleActionStartSettings" in data:
        import capo_medialive.types.follow_mode_schedule_action_start_settings

        out["follow_mode_schedule_action_start_settings"] = (
            capo_medialive.types.follow_mode_schedule_action_start_settings.deserialize_json(
                data["followModeScheduleActionStartSettings"]
            )
        )
    if "immediateModeScheduleActionStartSettings" in data:
        import capo_medialive.types.immediate_mode_schedule_action_start_settings

        out["immediate_mode_schedule_action_start_settings"] = (
            capo_medialive.types.immediate_mode_schedule_action_start_settings.deserialize_json(
                data["immediateModeScheduleActionStartSettings"]
            )
        )
    return out
