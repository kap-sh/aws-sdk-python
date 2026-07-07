"""Generated from Smithy shape ``com.amazonaws.medialive#StaticImageOutputDeactivateScheduleActionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min0
    import aws_sdk_medialive.types.__integer_min0_max7
    import aws_sdk_medialive.types.__list_of__string


class StaticImageOutputDeactivateScheduleActionSettings(TypedDict, closed=True):
    fade_out: NotRequired["aws_sdk_medialive.types.__integer_min0.__integerMin0"]
    """The time in milliseconds for the image to fade out. Default is 0 (no fade-out)."""
    layer: NotRequired["aws_sdk_medialive.types.__integer_min0_max7.__integerMin0Max7"]
    """The image overlay layer to deactivate, 0 to 7. Default is 0."""
    output_names: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """The name(s) of the output(s) the deactivation should apply to."""


# --- restJson1 ser/de ---
def serialize_json(value: StaticImageOutputDeactivateScheduleActionSettings) -> dict:
    out: dict = {}
    if "fade_out" in value:
        out["fadeOut"] = value["fade_out"]
    if "layer" in value:
        out["layer"] = value["layer"]
    if "output_names" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["outputNames"] = aws_sdk_medialive.types.__list_of__string.serialize_json(
            value["output_names"]
        )
    return out


def deserialize_json(data: dict) -> StaticImageOutputDeactivateScheduleActionSettings:
    out: StaticImageOutputDeactivateScheduleActionSettings = {}  # type: ignore[typeddict-item]
    if "fadeOut" in data:
        out["fade_out"] = data["fadeOut"]
    if "layer" in data:
        out["layer"] = data["layer"]
    if "outputNames" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["output_names"] = (
            aws_sdk_medialive.types.__list_of__string.deserialize_json(
                data["outputNames"]
            )
        )
    return out
