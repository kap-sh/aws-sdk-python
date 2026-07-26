"""Generated from Smithy shape ``com.amazonaws.medialive#AudioSelector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string_min1
    import capo_medialive.types.audio_selector_settings


class AudioSelector(TypedDict, closed=True):
    name: NotRequired["capo_medialive.types.__string_min1.__stringMin1"]
    """The name of this AudioSelector. AudioDescriptions will use this name to uniquely identify this Selector. Selector names should be unique per input."""
    selector_settings: NotRequired[
        "capo_medialive.types.audio_selector_settings.AudioSelectorSettings"
    ]
    """The audio selector settings."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioSelector) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "selector_settings" in value:
        import capo_medialive.types.audio_selector_settings

        out["selectorSettings"] = (
            capo_medialive.types.audio_selector_settings.serialize_json(
                value["selector_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioSelector:
    out: AudioSelector = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "selectorSettings" in data:
        import capo_medialive.types.audio_selector_settings

        out["selector_settings"] = (
            capo_medialive.types.audio_selector_settings.deserialize_json(
                data["selectorSettings"]
            )
        )
    return out
