"""Generated from Smithy shape ``com.amazonaws.medialive#StaticImageDeactivateScheduleActionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min0
    import capo_medialive.types.__integer_min0_max7


class StaticImageDeactivateScheduleActionSettings(TypedDict, closed=True):
    fade_out: NotRequired["capo_medialive.types.__integer_min0.__integerMin0"]
    """The time in milliseconds for the image to fade out. Default is 0 (no fade-out)."""
    layer: NotRequired["capo_medialive.types.__integer_min0_max7.__integerMin0Max7"]
    """The image overlay layer to deactivate, 0 to 7. Default is 0."""


# --- restJson1 ser/de ---
def serialize_json(value: StaticImageDeactivateScheduleActionSettings) -> dict:
    out: dict = {}
    if "fade_out" in value:
        out["fadeOut"] = value["fade_out"]
    if "layer" in value:
        out["layer"] = value["layer"]
    return out


def deserialize_json(data: dict) -> StaticImageDeactivateScheduleActionSettings:
    out: StaticImageDeactivateScheduleActionSettings = {}  # type: ignore[typeddict-item]
    if "fadeOut" in data:
        out["fade_out"] = data["fadeOut"]
    if "layer" in data:
        out["layer"] = data["layer"]
    return out
