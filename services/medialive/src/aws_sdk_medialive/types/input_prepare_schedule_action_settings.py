"""Generated from Smithy shape ``com.amazonaws.medialive#InputPrepareScheduleActionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of__string
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.input_clipping_settings


class InputPrepareScheduleActionSettings(TypedDict, closed=True):
    input_attachment_name_reference: NotRequired[
        "aws_sdk_medialive.types.__string.__string"
    ]
    """The name of the input attachment that should be prepared by this action. If no name is provided, the action will stop the most recent prepare (if any) when activated."""
    input_clipping_settings: NotRequired[
        "aws_sdk_medialive.types.input_clipping_settings.InputClippingSettings"
    ]
    """Settings to let you create a clip of the file input, in order to set up the input to ingest only a portion of the file."""
    url_path: NotRequired["aws_sdk_medialive.types.__list_of__string.__listOf__string"]
    """The value for the variable portion of the URL for the dynamic input, for this instance of the input. Each time you use the same dynamic input in an input switch action, you can provide a different value, in order to connect the input to a different content source."""


# --- restJson1 ser/de ---
def serialize_json(value: InputPrepareScheduleActionSettings) -> dict:
    out: dict = {}
    if "input_attachment_name_reference" in value:
        out["inputAttachmentNameReference"] = value["input_attachment_name_reference"]
    if "input_clipping_settings" in value:
        import aws_sdk_medialive.types.input_clipping_settings

        out["inputClippingSettings"] = (
            aws_sdk_medialive.types.input_clipping_settings.serialize_json(
                value["input_clipping_settings"]
            )
        )
    if "url_path" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["urlPath"] = aws_sdk_medialive.types.__list_of__string.serialize_json(
            value["url_path"]
        )
    return out


def deserialize_json(data: dict) -> InputPrepareScheduleActionSettings:
    out: InputPrepareScheduleActionSettings = {}  # type: ignore[typeddict-item]
    if "inputAttachmentNameReference" in data:
        out["input_attachment_name_reference"] = data["inputAttachmentNameReference"]
    if "inputClippingSettings" in data:
        import aws_sdk_medialive.types.input_clipping_settings

        out["input_clipping_settings"] = (
            aws_sdk_medialive.types.input_clipping_settings.deserialize_json(
                data["inputClippingSettings"]
            )
        )
    if "urlPath" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["url_path"] = aws_sdk_medialive.types.__list_of__string.deserialize_json(
            data["urlPath"]
        )
    return out
