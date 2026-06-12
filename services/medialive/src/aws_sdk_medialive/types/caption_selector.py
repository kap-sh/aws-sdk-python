"""Generated from Smithy shape ``com.amazonaws.medialive#CaptionSelector``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.__string_min1
    import aws_sdk_medialive.types.caption_selector_settings


class CaptionSelector(TypedDict):
    language_code: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """When specified this field indicates the three letter language code of the caption track to extract from the source."""
    name: NotRequired["aws_sdk_medialive.types.__string_min1.__stringMin1"]
    """Name identifier for a caption selector. This name is used to associate this caption selector with one or more caption descriptions. Names must be unique within an event."""
    selector_settings: NotRequired[
        "aws_sdk_medialive.types.caption_selector_settings.CaptionSelectorSettings"
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
        import aws_sdk_medialive.types.caption_selector_settings

        out["selectorSettings"] = (
            aws_sdk_medialive.types.caption_selector_settings.serialize_json(
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
        import aws_sdk_medialive.types.caption_selector_settings

        out["selector_settings"] = (
            aws_sdk_medialive.types.caption_selector_settings.deserialize_json(
                data["selectorSettings"]
            )
        )
    return out
