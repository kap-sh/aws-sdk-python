"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CodecMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer
    import capo_mediaconvert.types.__string
    import capo_mediaconvert.types.color_primaries
    import capo_mediaconvert.types.content_light_level
    import capo_mediaconvert.types.frame_rate
    import capo_mediaconvert.types.matrix_coefficients
    import capo_mediaconvert.types.transfer_characteristics


class CodecMetadata(TypedDict, closed=True):
    bit_depth: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """The number of bits used per color component in the video essence such as 8, 10, or 12 bits. Standard range (SDR) video typically uses 8-bit, while 10-bit is common for high dynamic range (HDR)."""
    chroma_subsampling: NotRequired["capo_mediaconvert.types.__string.__string"]
    r"""The chroma subsampling format used in the video encoding, such as \"4:2:0\" or \"4:4:4\". This describes how color information is sampled relative to brightness information. Different subsampling ratios affect video quality and file size, with \"4:4:4\" providing the highest color fidelity and \"4:2:0\" being most common for standard video."""
    coded_frame_rate: NotRequired["capo_mediaconvert.types.frame_rate.FrameRate"]
    """The frame rate of the video or audio track, expressed as a fraction with numerator and denominator values."""
    color_primaries: NotRequired[
        "capo_mediaconvert.types.color_primaries.ColorPrimaries"
    ]
    """The color space primaries of the video track, defining the red, green, and blue color coordinates used for the video. This information helps ensure accurate color reproduction during playback and transcoding."""
    content_light_level: NotRequired[
        "capo_mediaconvert.types.content_light_level.ContentLightLevel"
    ]
    """Content light level information (CTA-861.3). Describes the light level characteristics of the content."""
    height: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """The height in pixels as coded by the codec. This represents the actual encoded video height as specified in the video stream headers."""
    level: NotRequired["capo_mediaconvert.types.__string.__string"]
    """The codec level or tier that specifies the maximum processing requirements and capabilities. Levels define constraints such as maximum bit rate, frame rate, and resolution."""
    matrix_coefficients: NotRequired[
        "capo_mediaconvert.types.matrix_coefficients.MatrixCoefficients"
    ]
    """The color space matrix coefficients of the video track, defining how RGB color values are converted to and from YUV color space. This affects color accuracy during encoding and decoding processes."""
    profile: NotRequired["capo_mediaconvert.types.__string.__string"]
    """The codec profile used to encode the video. Profiles define specific feature sets and capabilities within a codec standard. For example, H.264 profiles include Baseline, Main, and High, each supporting different encoding features and complexity levels."""
    rotation: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """The clockwise rotation angle of the video, in degrees, as specified in the codec bitstream via a Display Orientation SEI message (payload type 47 for both H.264 and H.265). This field is null when the video essence does not contain a Display Orientation SEI message or when the rotation is 0 degrees."""
    scan_type: NotRequired["capo_mediaconvert.types.__string.__string"]
    """The scanning method specified in the video essence, indicating whether the video uses progressive or interlaced scanning."""
    transfer_characteristics: NotRequired[
        "capo_mediaconvert.types.transfer_characteristics.TransferCharacteristics"
    ]
    """The color space transfer characteristics of the video track, defining the relationship between linear light values and the encoded signal values. This affects brightness and contrast reproduction."""
    width: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """The width in pixels as coded by the codec. This represents the actual encoded video width as specified in the video stream headers."""


# --- restJson1 ser/de ---
def serialize_json(value: CodecMetadata) -> dict:
    out: dict = {}
    if "bit_depth" in value:
        out["bitDepth"] = value["bit_depth"]
    if "chroma_subsampling" in value:
        out["chromaSubsampling"] = value["chroma_subsampling"]
    if "coded_frame_rate" in value:
        import capo_mediaconvert.types.frame_rate

        out["codedFrameRate"] = capo_mediaconvert.types.frame_rate.serialize_json(
            value["coded_frame_rate"]
        )
    if "color_primaries" in value:
        import capo_mediaconvert.types.color_primaries

        out["colorPrimaries"] = capo_mediaconvert.types.color_primaries.serialize_json(
            value["color_primaries"]
        )
    if "content_light_level" in value:
        import capo_mediaconvert.types.content_light_level

        out["contentLightLevel"] = (
            capo_mediaconvert.types.content_light_level.serialize_json(
                value["content_light_level"]
            )
        )
    if "height" in value:
        out["height"] = value["height"]
    if "level" in value:
        out["level"] = value["level"]
    if "matrix_coefficients" in value:
        import capo_mediaconvert.types.matrix_coefficients

        out["matrixCoefficients"] = (
            capo_mediaconvert.types.matrix_coefficients.serialize_json(
                value["matrix_coefficients"]
            )
        )
    if "profile" in value:
        out["profile"] = value["profile"]
    if "rotation" in value:
        out["rotation"] = value["rotation"]
    if "scan_type" in value:
        out["scanType"] = value["scan_type"]
    if "transfer_characteristics" in value:
        import capo_mediaconvert.types.transfer_characteristics

        out["transferCharacteristics"] = (
            capo_mediaconvert.types.transfer_characteristics.serialize_json(
                value["transfer_characteristics"]
            )
        )
    if "width" in value:
        out["width"] = value["width"]
    return out


def deserialize_json(data: dict) -> CodecMetadata:
    out: CodecMetadata = {}  # type: ignore[typeddict-item]
    if "bitDepth" in data:
        out["bit_depth"] = data["bitDepth"]
    if "chromaSubsampling" in data:
        out["chroma_subsampling"] = data["chromaSubsampling"]
    if "codedFrameRate" in data:
        import capo_mediaconvert.types.frame_rate

        out["coded_frame_rate"] = capo_mediaconvert.types.frame_rate.deserialize_json(
            data["codedFrameRate"]
        )
    if "colorPrimaries" in data:
        import capo_mediaconvert.types.color_primaries

        out["color_primaries"] = (
            capo_mediaconvert.types.color_primaries.deserialize_json(
                data["colorPrimaries"]
            )
        )
    if "contentLightLevel" in data:
        import capo_mediaconvert.types.content_light_level

        out["content_light_level"] = (
            capo_mediaconvert.types.content_light_level.deserialize_json(
                data["contentLightLevel"]
            )
        )
    if "height" in data:
        out["height"] = data["height"]
    if "level" in data:
        out["level"] = data["level"]
    if "matrixCoefficients" in data:
        import capo_mediaconvert.types.matrix_coefficients

        out["matrix_coefficients"] = (
            capo_mediaconvert.types.matrix_coefficients.deserialize_json(
                data["matrixCoefficients"]
            )
        )
    if "profile" in data:
        out["profile"] = data["profile"]
    if "rotation" in data:
        out["rotation"] = data["rotation"]
    if "scanType" in data:
        out["scan_type"] = data["scanType"]
    if "transferCharacteristics" in data:
        import capo_mediaconvert.types.transfer_characteristics

        out["transfer_characteristics"] = (
            capo_mediaconvert.types.transfer_characteristics.deserialize_json(
                data["transferCharacteristics"]
            )
        )
    if "width" in data:
        out["width"] = data["width"]
    return out
