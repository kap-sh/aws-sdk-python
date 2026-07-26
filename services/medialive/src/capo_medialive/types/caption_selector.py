"""Generated from Smithy shape ``com.amazonaws.medialive#CaptionSelector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.__string_min1
    import capo_medialive.types.caption_selector_settings


class CaptionSelector(TypedDict, closed=True):
    language_code: NotRequired["capo_medialive.types.__string.__string"]
    """When specified this field indicates the three letter language code of the caption track to extract from the source."""
    name: NotRequired["capo_medialive.types.__string_min1.__stringMin1"]
    """Name identifier for a caption selector. This name is used to associate this caption selector with one or more caption descriptions. Names must be unique within an event."""
    selector_settings: NotRequired[
        "capo_medialive.types.caption_selector_settings.CaptionSelectorSettings"
    ]
    """Caption selector settings."""


# --- restJson1 ser/de ---
def serialize_json(value: CaptionSelector) -> dict:
    out: dict = {}
    if "language_code" in value:
        out["languageCode"] = value["language_code"]
    if "name" in value:
        out["name"] = value["name"]
    if "selector_settings" in value:
        import capo_medialive.types.caption_selector_settings

        out["selectorSettings"] = (
            capo_medialive.types.caption_selector_settings.serialize_json(
                value["selector_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> CaptionSelector:
    out: CaptionSelector = {}  # type: ignore[typeddict-item]
    if "languageCode" in data:
        out["language_code"] = data["languageCode"]
    if "name" in data:
        out["name"] = data["name"]
    if "selectorSettings" in data:
        import capo_medialive.types.caption_selector_settings

        out["selector_settings"] = (
            capo_medialive.types.caption_selector_settings.deserialize_json(
                data["selectorSettings"]
            )
        )
    return out
