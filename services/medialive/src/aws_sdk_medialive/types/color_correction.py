"""Generated from Smithy shape ``com.amazonaws.medialive#ColorCorrection``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.color_space


class ColorCorrection(TypedDict):
    input_color_space: NotRequired["aws_sdk_medialive.types.color_space.ColorSpace"]
    """The color space of the input."""
    output_color_space: NotRequired["aws_sdk_medialive.types.color_space.ColorSpace"]
    """The color space of the output."""
    uri: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The URI of the 3D LUT file. The protocol must be 's3:' or 's3ssl:':."""


# --- restJson1 ser/de ---
def serialize_json(value: ColorCorrection) -> dict:
    out: dict = {}
    if "input_color_space" in value:
        import aws_sdk_medialive.types.color_space

        out["inputColorSpace"] = aws_sdk_medialive.types.color_space.serialize_json(
            value["input_color_space"]
        )
    if "output_color_space" in value:
        import aws_sdk_medialive.types.color_space

        out["outputColorSpace"] = aws_sdk_medialive.types.color_space.serialize_json(
            value["output_color_space"]
        )
    if "uri" in value:
        out["uri"] = value["uri"]
    return out


def deserialize_json(data: dict) -> ColorCorrection:
    out: ColorCorrection = {}  # type: ignore[typeddict-item]
    if "inputColorSpace" in data:
        import aws_sdk_medialive.types.color_space

        out["input_color_space"] = aws_sdk_medialive.types.color_space.deserialize_json(
            data["inputColorSpace"]
        )
    if "outputColorSpace" in data:
        import aws_sdk_medialive.types.color_space

        out["output_color_space"] = (
            aws_sdk_medialive.types.color_space.deserialize_json(
                data["outputColorSpace"]
            )
        )
    if "uri" in data:
        out["uri"] = data["uri"]
    return out
