"""Generated from Smithy shape ``com.amazonaws.medialive#TimecodeBurninSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string_max255
    import capo_medialive.types.timecode_burnin_font_size
    import capo_medialive.types.timecode_burnin_position


class TimecodeBurninSettings(TypedDict, closed=True):
    font_size: NotRequired[
        "capo_medialive.types.timecode_burnin_font_size.TimecodeBurninFontSize"
    ]
    """Choose a timecode burn-in font size"""
    position: NotRequired[
        "capo_medialive.types.timecode_burnin_position.TimecodeBurninPosition"
    ]
    """Choose a timecode burn-in output position"""
    prefix: NotRequired["capo_medialive.types.__string_max255.__stringMax255"]
    """Create a timecode burn-in prefix (optional)"""


# --- restJson1 ser/de ---
def serialize_json(value: TimecodeBurninSettings) -> dict:
    out: dict = {}
    if "font_size" in value:
        import capo_medialive.types.timecode_burnin_font_size

        out["fontSize"] = capo_medialive.types.timecode_burnin_font_size.serialize_json(
            value["font_size"]
        )
    if "position" in value:
        import capo_medialive.types.timecode_burnin_position

        out["position"] = capo_medialive.types.timecode_burnin_position.serialize_json(
            value["position"]
        )
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> TimecodeBurninSettings:
    out: TimecodeBurninSettings = {}  # type: ignore[typeddict-item]
    if "fontSize" in data:
        import capo_medialive.types.timecode_burnin_font_size

        out["font_size"] = (
            capo_medialive.types.timecode_burnin_font_size.deserialize_json(
                data["fontSize"]
            )
        )
    if "position" in data:
        import capo_medialive.types.timecode_burnin_position

        out["position"] = (
            capo_medialive.types.timecode_burnin_position.deserialize_json(
                data["position"]
            )
        )
    if "prefix" in data:
        out["prefix"] = data["prefix"]
    return out
