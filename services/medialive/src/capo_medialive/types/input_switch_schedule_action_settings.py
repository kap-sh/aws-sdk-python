"""Generated from Smithy shape ``com.amazonaws.medialive#InputSwitchScheduleActionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of__string
    import capo_medialive.types.__string
    import capo_medialive.types.input_clipping_settings


class InputSwitchScheduleActionSettings(TypedDict, closed=True):
    input_attachment_name_reference: NotRequired[
        "capo_medialive.types.__string.__string"
    ]
    """The name of the input attachment (not the name of the input!) to switch to. The name is specified in the channel configuration."""
    input_clipping_settings: NotRequired[
        "capo_medialive.types.input_clipping_settings.InputClippingSettings"
    ]
    """Settings to let you create a clip of the file input, in order to set up the input to ingest only a portion of the file."""
    url_path: NotRequired["capo_medialive.types.__list_of__string.__listOf__string"]
    """The value for the variable portion of the URL for the dynamic input, for this instance of the input. Each time you use the same dynamic input in an input switch action, you can provide a different value, in order to connect the input to a different content source."""


# --- restJson1 ser/de ---
def serialize_json(value: InputSwitchScheduleActionSettings) -> dict:
    out: dict = {}
    if "input_attachment_name_reference" in value:
        out["inputAttachmentNameReference"] = value["input_attachment_name_reference"]
    if "input_clipping_settings" in value:
        import capo_medialive.types.input_clipping_settings

        out["inputClippingSettings"] = (
            capo_medialive.types.input_clipping_settings.serialize_json(
                value["input_clipping_settings"]
            )
        )
    if "url_path" in value:
        import capo_medialive.types.__list_of__string

        out["urlPath"] = capo_medialive.types.__list_of__string.serialize_json(
            value["url_path"]
        )
    return out


def deserialize_json(data: dict) -> InputSwitchScheduleActionSettings:
    out: InputSwitchScheduleActionSettings = {}  # type: ignore[typeddict-item]
    if "inputAttachmentNameReference" in data:
        out["input_attachment_name_reference"] = data["inputAttachmentNameReference"]
    if "inputClippingSettings" in data:
        import capo_medialive.types.input_clipping_settings

        out["input_clipping_settings"] = (
            capo_medialive.types.input_clipping_settings.deserialize_json(
                data["inputClippingSettings"]
            )
        )
    if "urlPath" in data:
        import capo_medialive.types.__list_of__string

        out["url_path"] = capo_medialive.types.__list_of__string.deserialize_json(
            data["urlPath"]
        )
    return out
