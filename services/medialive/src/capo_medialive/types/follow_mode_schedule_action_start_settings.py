"""Generated from Smithy shape ``com.amazonaws.medialive#FollowModeScheduleActionStartSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.follow_point


class FollowModeScheduleActionStartSettings(TypedDict, closed=True):
    follow_point: NotRequired["capo_medialive.types.follow_point.FollowPoint"]
    """Identifies whether this action starts relative to the start or relative to the end of the reference action."""
    reference_action_name: NotRequired["capo_medialive.types.__string.__string"]
    """The action name of another action that this one refers to."""


# --- restJson1 ser/de ---
def serialize_json(value: FollowModeScheduleActionStartSettings) -> dict:
    out: dict = {}
    if "follow_point" in value:
        import capo_medialive.types.follow_point

        out["followPoint"] = capo_medialive.types.follow_point.serialize_json(
            value["follow_point"]
        )
    if "reference_action_name" in value:
        out["referenceActionName"] = value["reference_action_name"]
    return out


def deserialize_json(data: dict) -> FollowModeScheduleActionStartSettings:
    out: FollowModeScheduleActionStartSettings = {}  # type: ignore[typeddict-item]
    if "followPoint" in data:
        import capo_medialive.types.follow_point

        out["follow_point"] = capo_medialive.types.follow_point.deserialize_json(
            data["followPoint"]
        )
    if "referenceActionName" in data:
        out["reference_action_name"] = data["referenceActionName"]
    return out
