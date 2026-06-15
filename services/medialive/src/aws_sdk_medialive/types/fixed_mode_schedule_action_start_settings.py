"""Generated from Smithy shape ``com.amazonaws.medialive#FixedModeScheduleActionStartSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class FixedModeScheduleActionStartSettings(TypedDict):
    time: NotRequired["aws_sdk_medialive.types.__string.__string"]
    r"""Start time for the action to start in the channel. (Not the time for the action to be added to the schedule: actions are always added to the schedule immediately.) UTC format: yyyy-mm-ddThh:mm:ss.nnnZ. All the letters are digits (for example, mm might be 01) except for the two constants \"T\" for time and \"Z\" for \"UTC format\"."""


# --- restJson1 ser/de ---
def serialize_json(value: FixedModeScheduleActionStartSettings) -> dict:
    out: dict = {}
    if "time" in value:
        out["time"] = value["time"]
    return out


def deserialize_json(data: dict) -> FixedModeScheduleActionStartSettings:
    out: FixedModeScheduleActionStartSettings = {}  # type: ignore[typeddict-item]
    if "time" in data:
        out["time"] = data["time"]
    return out
