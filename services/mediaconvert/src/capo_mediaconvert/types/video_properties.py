"""Generated from Smithy shape ``com.amazonaws.mediaconvert#VideoProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer
    import capo_mediaconvert.types.__long
    import capo_mediaconvert.types.codec_metadata
    import capo_mediaconvert.types.color_primaries
    import capo_mediaconvert.types.frame_rate
    import capo_mediaconvert.types.hdr_metadata
    import capo_mediaconvert.types.matrix_coefficients
    import capo_mediaconvert.types.transfer_characteristics


class VideoProperties(TypedDict, closed=True):
    bit_depth: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """The number of bits used per color component such as 8, 10, or 12 bits. Standard range (SDR) video typically uses 8-bit, while 10-bit is common for high dynamic range (HDR)."""
    bit_rate: NotRequired["capo_mediaconvert.types.__long.__long"]
    """The bit rate of the video track, in bits per second."""
    codec_metadata: NotRequired["capo_mediaconvert.types.codec_metadata.CodecMetadata"]
    """Codec-specific parameters parsed from the video essence headers. This information provides detailed technical specifications about how the video was encoded, including profile settings, resolution details, and color space information that can help you understand the source video characteristics and make informed encoding decisions."""
    color_primaries: NotRequired[
        "capo_mediaconvert.types.color_primaries.ColorPrimaries"
    ]
    """The color space primaries of the video track, defining the red, green, and blue color coordinates used for the video. This information helps ensure accurate color reproduction during playback and transcoding."""
    frame_rate: NotRequired["capo_mediaconvert.types.frame_rate.FrameRate"]
    """The frame rate of the video or audio track, expressed as a fraction with numerator and denominator values."""
    hdr_metadata: NotRequired["capo_mediaconvert.types.hdr_metadata.HdrMetadata"]
    """HDR (High Dynamic Range) metadata extracted from the container, including mastering display color volume and content light level information. This metadata is present in HDR10 and similar HDR content."""
    height: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """The height of the video track, in pixels."""
    matrix_coefficients: NotRequired[
        "capo_mediaconvert.types.matrix_coefficients.MatrixCoefficients"
    ]
    """The color space matrix coefficients of the video track, defining how RGB color values are converted to and from YUV color space. This affects color accuracy during encoding and decoding processes."""
    rotation: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """The clockwise rotation angle of the video track, in degrees, as derived from container-level metadata (e.g. the MP4 tkhd transformation matrix or the Matroska ProjectionPoseRoll element). Common values are 90, 180, and 270. This field is null when no rotation metadata is present or when the rotation is 0 degrees. For MP4, non-standard transformation matrices also yield null."""
    transfer_characteristics: NotRequired[
        "capo_mediaconvert.types.transfer_characteristics.TransferCharacteristics"
    ]
    """The color space transfer characteristics of the video track, defining the relationship between linear light values and the encoded signal values. This affects brightness and contrast reproduction."""
    width: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """The width of the video track, in pixels."""


# --- restJson1 ser/de ---
def serialize_json(value: VideoProperties) -> dict:
    out: dict = {}
    if "bit_depth" in value:
        out["bitDepth"] = value["bit_depth"]
    if "bit_rate" in value:
        out["bitRate"] = value["bit_rate"]
    if "codec_metadata" in value:
        import capo_mediaconvert.types.codec_metadata

        out["codecMetadata"] = capo_mediaconvert.types.codec_metadata.serialize_json(
            value["codec_metadata"]
        )
    if "color_primaries" in value:
        import capo_mediaconvert.types.color_primaries

        out["colorPrimaries"] = capo_mediaconvert.types.color_primaries.serialize_json(
            value["color_primaries"]
        )
    if "frame_rate" in value:
        import capo_mediaconvert.types.frame_rate

        out["frameRate"] = capo_mediaconvert.types.frame_rate.serialize_json(
            value["frame_rate"]
        )
    if "hdr_metadata" in value:
        import capo_mediaconvert.types.hdr_metadata

        out["hdrMetadata"] = capo_mediaconvert.types.hdr_metadata.serialize_json(
            value["hdr_metadata"]
        )
    if "height" in value:
        out["height"] = value["height"]
    if "matrix_coefficients" in value:
        import capo_mediaconvert.types.matrix_coefficients

        out["matrixCoefficients"] = (
            capo_mediaconvert.types.matrix_coefficients.serialize_json(
                value["matrix_coefficients"]
            )
        )
    if "rotation" in value:
        out["rotation"] = value["rotation"]
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


def deserialize_json(data: dict) -> VideoProperties:
    out: VideoProperties = {}  # type: ignore[typeddict-item]
    if "bitDepth" in data:
        out["bit_depth"] = data["bitDepth"]
    if "bitRate" in data:
        out["bit_rate"] = data["bitRate"]
    if "codecMetadata" in data:
        import capo_mediaconvert.types.codec_metadata

        out["codec_metadata"] = capo_mediaconvert.types.codec_metadata.deserialize_json(
            data["codecMetadata"]
        )
    if "colorPrimaries" in data:
        import capo_mediaconvert.types.color_primaries

        out["color_primaries"] = (
            capo_mediaconvert.types.color_primaries.deserialize_json(
                data["colorPrimaries"]
            )
        )
    if "frameRate" in data:
        import capo_mediaconvert.types.frame_rate

        out["frame_rate"] = capo_mediaconvert.types.frame_rate.deserialize_json(
            data["frameRate"]
        )
    if "hdrMetadata" in data:
        import capo_mediaconvert.types.hdr_metadata

        out["hdr_metadata"] = capo_mediaconvert.types.hdr_metadata.deserialize_json(
            data["hdrMetadata"]
        )
    if "height" in data:
        out["height"] = data["height"]
    if "matrixCoefficients" in data:
        import capo_mediaconvert.types.matrix_coefficients

        out["matrix_coefficients"] = (
            capo_mediaconvert.types.matrix_coefficients.deserialize_json(
                data["matrixCoefficients"]
            )
        )
    if "rotation" in data:
        out["rotation"] = data["rotation"]
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
