"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ColorCorrector``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min0_max2147483647
    import aws_sdk_mediaconvert.types.__integer_min1_max100
    import aws_sdk_mediaconvert.types.__integer_min100_max1000
    import aws_sdk_mediaconvert.types.__integer_min_negative180_max180
    import aws_sdk_mediaconvert.types.clip_limits
    import aws_sdk_mediaconvert.types.color_space_conversion
    import aws_sdk_mediaconvert.types.hdr10_metadata
    import aws_sdk_mediaconvert.types.hdr_to_sdr_tone_mapper
    import aws_sdk_mediaconvert.types.sample_range_conversion


class ColorCorrector(TypedDict):
    brightness: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max100.__integerMin1Max100"
    ]
    """Brightness level."""
    clip_limits: NotRequired["aws_sdk_mediaconvert.types.clip_limits.ClipLimits"]
    """Specify YUV limits and RGB tolerances when you set Sample range conversion to Limited range clip."""
    color_space_conversion: NotRequired[
        "aws_sdk_mediaconvert.types.color_space_conversion.ColorSpaceConversion"
    ]
    """Specify the color space you want for this output. The service supports conversion between HDR formats, between SDR formats, from SDR to HDR, and from HDR to SDR. SDR to HDR conversion doesn't upgrade the dynamic range. The converted video has an HDR format, but visually appears the same as an unconverted output. HDR to SDR conversion uses tone mapping to approximate the outcome of manually regrading from HDR to SDR. When you specify an output color space, MediaConvert uses the following color space metadata, which includes color primaries, transfer characteristics, and matrix coefficients: * HDR 10: BT.2020, PQ, BT.2020 non-constant * HLG 2020: BT.2020, HLG, BT.2020 non-constant * P3DCI (Theater): DCIP3, SMPTE 428M, BT.709 * P3D65 (SDR): Display P3, sRGB, BT.709 * P3D65 (HDR): Display P3, PQ, BT.709"""
    contrast: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max100.__integerMin1Max100"
    ]
    """Contrast level."""
    hdr10_metadata: NotRequired[
        "aws_sdk_mediaconvert.types.hdr10_metadata.Hdr10Metadata"
    ]
    """Use these settings when you convert to the HDR 10 color space. Specify the SMPTE ST 2086 Mastering Display Color Volume static metadata that you want signaled in the output. These values don't affect the pixel values that are encoded in the video stream. They are intended to help the downstream video player display content in a way that reflects the intentions of the the content creator. When you set Color space conversion to HDR 10, these settings are required. You must set values for Max frame average light level and Max content light level; these settings don't have a default value. The default values for the other HDR 10 metadata settings are defined by the P3D65 color space. For more information about MediaConvert HDR jobs, see https://docs.aws.amazon.com/console/mediaconvert/hdr."""
    hdr_to_sdr_tone_mapper: NotRequired[
        "aws_sdk_mediaconvert.types.hdr_to_sdr_tone_mapper.HDRToSDRToneMapper"
    ]
    """Specify how MediaConvert maps brightness and colors from your HDR input to your SDR output. The mode that you select represents a creative choice, with different tradeoffs in the details and tones of your output. To maintain details in bright or saturated areas of your output: Choose Preserve details. For some sources, your SDR output may look less bright and less saturated when compared to your HDR source. MediaConvert automatically applies this mode for HLG sources, regardless of your choice. For a bright and saturated output: Choose Vibrant. We recommend that you choose this mode when any of your source content is HDR10, and for the best results when it is mastered for 1000 nits. You may notice loss of details in bright or saturated areas of your output. HDR to SDR tone mapping has no effect when your input is SDR."""
    hue: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min_negative180_max180.__integerMinNegative180Max180"
    ]
    """Hue in degrees."""
    max_luminance: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Specify the maximum mastering display luminance. Enter an integer from 0 to 2147483647, in units of 0.0001 nits. For example, enter 10000000 for 1000 nits."""
    sample_range_conversion: NotRequired[
        "aws_sdk_mediaconvert.types.sample_range_conversion.SampleRangeConversion"
    ]
    """Specify how MediaConvert limits the color sample range for this output. To create a limited range output from a full range input: Choose Limited range squeeze. For full range inputs, MediaConvert performs a linear offset to color samples equally across all pixels and frames. Color samples in 10-bit outputs are limited to 64 through 940, and 8-bit outputs are limited to 16 through 235. Note: For limited range inputs, values for color samples are passed through to your output unchanged. MediaConvert does not limit the sample range. To correct pixels in your input that are out of range or out of gamut: Choose Limited range clip. Use for broadcast applications. MediaConvert conforms any pixels outside of the values that you specify under Minimum YUV and Maximum YUV to limited range bounds. MediaConvert also corrects any YUV values that, when converted to RGB, would be outside the bounds you specify under Minimum RGB tolerance and Maximum RGB tolerance. With either limited range conversion, MediaConvert writes the sample range metadata in the output."""
    saturation: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max100.__integerMin1Max100"
    ]
    """Saturation level."""
    sdr_reference_white_level: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min100_max1000.__integerMin100Max1000"
    ]
    """Specify the reference white level, in nits, for all of your SDR inputs. Use to correct brightness levels within HDR10 outputs. The following color metadata must be present in your SDR input: color primaries, transfer characteristics, and matrix coefficients. If your SDR input has missing color metadata, or if you want to correct input color metadata, manually specify a color space in the input video selector. For 1,000 nit peak brightness displays, we recommend that you set SDR reference white level to 203 (according to ITU-R BT.2408). Leave blank to use the default value of 100, or specify an integer from 100 to 1000."""


# --- restJson1 ser/de ---
def serialize_json(value: ColorCorrector) -> dict:
    out: dict = {}
    if "brightness" in value:
        out["brightness"] = value["brightness"]
    if "clip_limits" in value:
        import aws_sdk_mediaconvert.types.clip_limits

        out["clipLimits"] = aws_sdk_mediaconvert.types.clip_limits.serialize_json(
            value["clip_limits"]
        )
    if "color_space_conversion" in value:
        import aws_sdk_mediaconvert.types.color_space_conversion

        out["colorSpaceConversion"] = (
            aws_sdk_mediaconvert.types.color_space_conversion.serialize_json(
                value["color_space_conversion"]
            )
        )
    if "contrast" in value:
        out["contrast"] = value["contrast"]
    if "hdr10_metadata" in value:
        import aws_sdk_mediaconvert.types.hdr10_metadata

        out["hdr10Metadata"] = aws_sdk_mediaconvert.types.hdr10_metadata.serialize_json(
            value["hdr10_metadata"]
        )
    if "hdr_to_sdr_tone_mapper" in value:
        import aws_sdk_mediaconvert.types.hdr_to_sdr_tone_mapper

        out["hdrToSdrToneMapper"] = (
            aws_sdk_mediaconvert.types.hdr_to_sdr_tone_mapper.serialize_json(
                value["hdr_to_sdr_tone_mapper"]
            )
        )
    if "hue" in value:
        out["hue"] = value["hue"]
    if "max_luminance" in value:
        out["maxLuminance"] = value["max_luminance"]
    if "sample_range_conversion" in value:
        import aws_sdk_mediaconvert.types.sample_range_conversion

        out["sampleRangeConversion"] = (
            aws_sdk_mediaconvert.types.sample_range_conversion.serialize_json(
                value["sample_range_conversion"]
            )
        )
    if "saturation" in value:
        out["saturation"] = value["saturation"]
    if "sdr_reference_white_level" in value:
        out["sdrReferenceWhiteLevel"] = value["sdr_reference_white_level"]
    return out


def deserialize_json(data: dict) -> ColorCorrector:
    out: ColorCorrector = {}  # type: ignore[typeddict-item]
    if "brightness" in data:
        out["brightness"] = data["brightness"]
    if "clipLimits" in data:
        import aws_sdk_mediaconvert.types.clip_limits

        out["clip_limits"] = aws_sdk_mediaconvert.types.clip_limits.deserialize_json(
            data["clipLimits"]
        )
    if "colorSpaceConversion" in data:
        import aws_sdk_mediaconvert.types.color_space_conversion

        out["color_space_conversion"] = (
            aws_sdk_mediaconvert.types.color_space_conversion.deserialize_json(
                data["colorSpaceConversion"]
            )
        )
    if "contrast" in data:
        out["contrast"] = data["contrast"]
    if "hdr10Metadata" in data:
        import aws_sdk_mediaconvert.types.hdr10_metadata

        out["hdr10_metadata"] = (
            aws_sdk_mediaconvert.types.hdr10_metadata.deserialize_json(
                data["hdr10Metadata"]
            )
        )
    if "hdrToSdrToneMapper" in data:
        import aws_sdk_mediaconvert.types.hdr_to_sdr_tone_mapper

        out["hdr_to_sdr_tone_mapper"] = (
            aws_sdk_mediaconvert.types.hdr_to_sdr_tone_mapper.deserialize_json(
                data["hdrToSdrToneMapper"]
            )
        )
    if "hue" in data:
        out["hue"] = data["hue"]
    if "maxLuminance" in data:
        out["max_luminance"] = data["maxLuminance"]
    if "sampleRangeConversion" in data:
        import aws_sdk_mediaconvert.types.sample_range_conversion

        out["sample_range_conversion"] = (
            aws_sdk_mediaconvert.types.sample_range_conversion.deserialize_json(
                data["sampleRangeConversion"]
            )
        )
    if "saturation" in data:
        out["saturation"] = data["saturation"]
    if "sdrReferenceWhiteLevel" in data:
        out["sdr_reference_white_level"] = data["sdrReferenceWhiteLevel"]
    return out
