"""Generated from Smithy shape ``com.amazonaws.medialive#StaticImageOutputActivateScheduleActionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min0
    import aws_sdk_medialive.types.__integer_min0_max7
    import aws_sdk_medialive.types.__integer_min0_max100
    import aws_sdk_medialive.types.__integer_min1
    import aws_sdk_medialive.types.__list_of__string
    import aws_sdk_medialive.types.input_location


class StaticImageOutputActivateScheduleActionSettings(TypedDict, closed=True):
    duration: NotRequired["aws_sdk_medialive.types.__integer_min0.__integerMin0"]
    """The duration in milliseconds for the image to remain on the video. If omitted or set to 0 the duration is unlimited and the image will remain until it is explicitly deactivated."""
    fade_in: NotRequired["aws_sdk_medialive.types.__integer_min0.__integerMin0"]
    """The time in milliseconds for the image to fade in. The fade-in starts at the start time of the overlay. Default is 0 (no fade-in)."""
    fade_out: NotRequired["aws_sdk_medialive.types.__integer_min0.__integerMin0"]
    """Applies only if a duration is specified. The time in milliseconds for the image to fade out. The fade-out starts when the duration time is hit, so it effectively extends the duration. Default is 0 (no fade-out)."""
    height: NotRequired["aws_sdk_medialive.types.__integer_min1.__integerMin1"]
    """The height of the image when inserted into the video, in pixels. The overlay will be scaled up or down to the specified height. Leave blank to use the native height of the overlay."""
    image: NotRequired["aws_sdk_medialive.types.input_location.InputLocation"]
    """The location and filename of the image file to overlay on the video. The file must be a 32-bit BMP, PNG, or TGA file, and must not be larger (in pixels) than the input video."""
    image_x: NotRequired["aws_sdk_medialive.types.__integer_min0.__integerMin0"]
    """Placement of the left edge of the overlay relative to the left edge of the video frame, in pixels. 0 (the default) is the left edge of the frame. If the placement causes the overlay to extend beyond the right edge of the underlying video, then the overlay is cropped on the right."""
    image_y: NotRequired["aws_sdk_medialive.types.__integer_min0.__integerMin0"]
    """Placement of the top edge of the overlay relative to the top edge of the video frame, in pixels. 0 (the default) is the top edge of the frame. If the placement causes the overlay to extend beyond the bottom edge of the underlying video, then the overlay is cropped on the bottom."""
    layer: NotRequired["aws_sdk_medialive.types.__integer_min0_max7.__integerMin0Max7"]
    """The number of the layer, 0 to 7. There are 8 layers that can be overlaid on the video, each layer with a different image. The layers are in Z order, which means that overlays with higher values of layer are inserted on top of overlays with lower values of layer. Default is 0."""
    opacity: NotRequired[
        "aws_sdk_medialive.types.__integer_min0_max100.__integerMin0Max100"
    ]
    """Opacity of image where 0 is transparent and 100 is fully opaque. Default is 100."""
    output_names: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """The name(s) of the output(s) the activation should apply to."""
    width: NotRequired["aws_sdk_medialive.types.__integer_min1.__integerMin1"]
    """The width of the image when inserted into the video, in pixels. The overlay will be scaled up or down to the specified width. Leave blank to use the native width of the overlay."""


# --- restJson1 ser/de ---
def serialize_json(value: StaticImageOutputActivateScheduleActionSettings) -> dict:
    out: dict = {}
    if "duration" in value:
        out["duration"] = value["duration"]
    if "fade_in" in value:
        out["fadeIn"] = value["fade_in"]
    if "fade_out" in value:
        out["fadeOut"] = value["fade_out"]
    if "height" in value:
        out["height"] = value["height"]
    if "image" in value:
        import aws_sdk_medialive.types.input_location

        out["image"] = aws_sdk_medialive.types.input_location.serialize_json(
            value["image"]
        )
    if "image_x" in value:
        out["imageX"] = value["image_x"]
    if "image_y" in value:
        out["imageY"] = value["image_y"]
    if "layer" in value:
        out["layer"] = value["layer"]
    if "opacity" in value:
        out["opacity"] = value["opacity"]
    if "output_names" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["outputNames"] = aws_sdk_medialive.types.__list_of__string.serialize_json(
            value["output_names"]
        )
    if "width" in value:
        out["width"] = value["width"]
    return out


def deserialize_json(data: dict) -> StaticImageOutputActivateScheduleActionSettings:
    out: StaticImageOutputActivateScheduleActionSettings = {}  # type: ignore[typeddict-item]
    if "duration" in data:
        out["duration"] = data["duration"]
    if "fadeIn" in data:
        out["fade_in"] = data["fadeIn"]
    if "fadeOut" in data:
        out["fade_out"] = data["fadeOut"]
    if "height" in data:
        out["height"] = data["height"]
    if "image" in data:
        import aws_sdk_medialive.types.input_location

        out["image"] = aws_sdk_medialive.types.input_location.deserialize_json(
            data["image"]
        )
    if "imageX" in data:
        out["image_x"] = data["imageX"]
    if "imageY" in data:
        out["image_y"] = data["imageY"]
    if "layer" in data:
        out["layer"] = data["layer"]
    if "opacity" in data:
        out["opacity"] = data["opacity"]
    if "outputNames" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["output_names"] = (
            aws_sdk_medialive.types.__list_of__string.deserialize_json(
                data["outputNames"]
            )
        )
    if "width" in data:
        out["width"] = data["width"]
    return out
