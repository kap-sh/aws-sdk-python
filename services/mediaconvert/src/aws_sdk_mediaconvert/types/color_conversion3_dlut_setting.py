"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ColorConversion3DLUTSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min0_max2147483647
    import aws_sdk_mediaconvert.types.__string_min14_pattern_s3_cube_cube_https_cube_cube
    import aws_sdk_mediaconvert.types.color_space


class ColorConversion3DLUTSetting(TypedDict, closed=True):
    file_input: NotRequired[
        "aws_sdk_mediaconvert.types.__string_min14_pattern_s3_cube_cube_https_cube_cube.__stringMin14PatternS3CubeCUBEHttpsCubeCUBE"
    ]
    """Specify the input file S3, HTTP, or HTTPS URL for your 3D LUT .cube file. Note that MediaConvert accepts 3D LUT files up to 8MB in size."""
    input_color_space: NotRequired["aws_sdk_mediaconvert.types.color_space.ColorSpace"]
    """Specify which inputs use this 3D LUT, according to their color space."""
    input_mastering_luminance: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Specify which inputs use this 3D LUT, according to their luminance. To apply this 3D LUT to HDR10 or P3D65 (HDR) inputs with a specific mastering luminance: Enter an integer from 0 to 2147483647, corresponding to the input's Maximum luminance value. To apply this 3D LUT to any input regardless of its luminance: Leave blank, or enter 0."""
    output_color_space: NotRequired["aws_sdk_mediaconvert.types.color_space.ColorSpace"]
    """Specify which outputs use this 3D LUT, according to their color space."""
    output_mastering_luminance: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Specify which outputs use this 3D LUT, according to their luminance. To apply this 3D LUT to HDR10 or P3D65 (HDR) outputs with a specific luminance: Enter an integer from 0 to 2147483647, corresponding to the output's luminance. To apply this 3D LUT to any output regardless of its luminance: Leave blank, or enter 0."""


# --- restJson1 ser/de ---
def serialize_json(value: ColorConversion3DLUTSetting) -> dict:
    out: dict = {}
    if "file_input" in value:
        out["fileInput"] = value["file_input"]
    if "input_color_space" in value:
        import aws_sdk_mediaconvert.types.color_space

        out["inputColorSpace"] = aws_sdk_mediaconvert.types.color_space.serialize_json(
            value["input_color_space"]
        )
    if "input_mastering_luminance" in value:
        out["inputMasteringLuminance"] = value["input_mastering_luminance"]
    if "output_color_space" in value:
        import aws_sdk_mediaconvert.types.color_space

        out["outputColorSpace"] = aws_sdk_mediaconvert.types.color_space.serialize_json(
            value["output_color_space"]
        )
    if "output_mastering_luminance" in value:
        out["outputMasteringLuminance"] = value["output_mastering_luminance"]
    return out


def deserialize_json(data: dict) -> ColorConversion3DLUTSetting:
    out: ColorConversion3DLUTSetting = {}  # type: ignore[typeddict-item]
    if "fileInput" in data:
        out["file_input"] = data["fileInput"]
    if "inputColorSpace" in data:
        import aws_sdk_mediaconvert.types.color_space

        out["input_color_space"] = (
            aws_sdk_mediaconvert.types.color_space.deserialize_json(
                data["inputColorSpace"]
            )
        )
    if "inputMasteringLuminance" in data:
        out["input_mastering_luminance"] = data["inputMasteringLuminance"]
    if "outputColorSpace" in data:
        import aws_sdk_mediaconvert.types.color_space

        out["output_color_space"] = (
            aws_sdk_mediaconvert.types.color_space.deserialize_json(
                data["outputColorSpace"]
            )
        )
    if "outputMasteringLuminance" in data:
        out["output_mastering_luminance"] = data["outputMasteringLuminance"]
    return out
