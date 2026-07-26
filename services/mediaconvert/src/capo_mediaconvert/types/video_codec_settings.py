"""Generated from Smithy shape ``com.amazonaws.mediaconvert#VideoCodecSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.av1_settings
    import capo_mediaconvert.types.avc_intra_settings
    import capo_mediaconvert.types.frame_capture_settings
    import capo_mediaconvert.types.gif_settings
    import capo_mediaconvert.types.h264_settings
    import capo_mediaconvert.types.h265_settings
    import capo_mediaconvert.types.mpeg2_settings
    import capo_mediaconvert.types.passthrough_settings
    import capo_mediaconvert.types.prores_settings
    import capo_mediaconvert.types.uncompressed_settings
    import capo_mediaconvert.types.vc3_settings
    import capo_mediaconvert.types.video_codec
    import capo_mediaconvert.types.vp8_settings
    import capo_mediaconvert.types.vp9_settings
    import capo_mediaconvert.types.xavc_settings


class VideoCodecSettings(TypedDict, closed=True):
    av1_settings: NotRequired["capo_mediaconvert.types.av1_settings.Av1Settings"]
    """Required when you set Codec, under VideoDescription>CodecSettings to the value AV1."""
    avc_intra_settings: NotRequired[
        "capo_mediaconvert.types.avc_intra_settings.AvcIntraSettings"
    ]
    """Required when you choose AVC-Intra for your output video codec. For more information about the AVC-Intra settings, see the relevant specification. For detailed information about SD and HD in AVC-Intra, see https://ieeexplore.ieee.org/document/7290936. For information about 4K/2K in AVC-Intra, see https://pro-av.panasonic.net/en/avc-ultra/AVC-ULTRAoverview.pdf."""
    codec: NotRequired["capo_mediaconvert.types.video_codec.VideoCodec"]
    """Specifies the video codec. This must be equal to one of the enum values defined by the object VideoCodec. To passthrough the video stream of your input without any video encoding: Choose Passthrough. More information about passthrough codec support and job settings requirements, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/video-passthrough-feature-restrictions.html"""
    frame_capture_settings: NotRequired[
        "capo_mediaconvert.types.frame_capture_settings.FrameCaptureSettings"
    ]
    """Required when you set Codec to the value FRAME_CAPTURE."""
    gif_settings: NotRequired["capo_mediaconvert.types.gif_settings.GifSettings"]
    """Required when you set (Codec) under (VideoDescription)>(CodecSettings) to the value GIF"""
    h264_settings: NotRequired["capo_mediaconvert.types.h264_settings.H264Settings"]
    """Required when you set Codec to the value H_264."""
    h265_settings: NotRequired["capo_mediaconvert.types.h265_settings.H265Settings"]
    """Settings for H265 codec"""
    mpeg2_settings: NotRequired["capo_mediaconvert.types.mpeg2_settings.Mpeg2Settings"]
    """Required when you set Codec to the value MPEG2."""
    passthrough_settings: NotRequired[
        "capo_mediaconvert.types.passthrough_settings.PassthroughSettings"
    ]
    """Optional settings when you set Codec to the value Passthrough."""
    prores_settings: NotRequired[
        "capo_mediaconvert.types.prores_settings.ProresSettings"
    ]
    """Required when you set Codec to the value PRORES."""
    uncompressed_settings: NotRequired[
        "capo_mediaconvert.types.uncompressed_settings.UncompressedSettings"
    ]
    """Required when you set Codec, under VideoDescription>CodecSettings to the value UNCOMPRESSED."""
    vc3_settings: NotRequired["capo_mediaconvert.types.vc3_settings.Vc3Settings"]
    """Required when you set Codec to the value VC3"""
    vp8_settings: NotRequired["capo_mediaconvert.types.vp8_settings.Vp8Settings"]
    """Required when you set Codec to the value VP8."""
    vp9_settings: NotRequired["capo_mediaconvert.types.vp9_settings.Vp9Settings"]
    """Required when you set Codec to the value VP9."""
    xavc_settings: NotRequired["capo_mediaconvert.types.xavc_settings.XavcSettings"]
    """Required when you set Codec to the value XAVC."""


# --- restJson1 ser/de ---
def serialize_json(value: VideoCodecSettings) -> dict:
    out: dict = {}
    if "av1_settings" in value:
        import capo_mediaconvert.types.av1_settings

        out["av1Settings"] = capo_mediaconvert.types.av1_settings.serialize_json(
            value["av1_settings"]
        )
    if "avc_intra_settings" in value:
        import capo_mediaconvert.types.avc_intra_settings

        out["avcIntraSettings"] = (
            capo_mediaconvert.types.avc_intra_settings.serialize_json(
                value["avc_intra_settings"]
            )
        )
    if "codec" in value:
        import capo_mediaconvert.types.video_codec

        out["codec"] = capo_mediaconvert.types.video_codec.serialize_json(
            value["codec"]
        )
    if "frame_capture_settings" in value:
        import capo_mediaconvert.types.frame_capture_settings

        out["frameCaptureSettings"] = (
            capo_mediaconvert.types.frame_capture_settings.serialize_json(
                value["frame_capture_settings"]
            )
        )
    if "gif_settings" in value:
        import capo_mediaconvert.types.gif_settings

        out["gifSettings"] = capo_mediaconvert.types.gif_settings.serialize_json(
            value["gif_settings"]
        )
    if "h264_settings" in value:
        import capo_mediaconvert.types.h264_settings

        out["h264Settings"] = capo_mediaconvert.types.h264_settings.serialize_json(
            value["h264_settings"]
        )
    if "h265_settings" in value:
        import capo_mediaconvert.types.h265_settings

        out["h265Settings"] = capo_mediaconvert.types.h265_settings.serialize_json(
            value["h265_settings"]
        )
    if "mpeg2_settings" in value:
        import capo_mediaconvert.types.mpeg2_settings

        out["mpeg2Settings"] = capo_mediaconvert.types.mpeg2_settings.serialize_json(
            value["mpeg2_settings"]
        )
    if "passthrough_settings" in value:
        import capo_mediaconvert.types.passthrough_settings

        out["passthroughSettings"] = (
            capo_mediaconvert.types.passthrough_settings.serialize_json(
                value["passthrough_settings"]
            )
        )
    if "prores_settings" in value:
        import capo_mediaconvert.types.prores_settings

        out["proresSettings"] = capo_mediaconvert.types.prores_settings.serialize_json(
            value["prores_settings"]
        )
    if "uncompressed_settings" in value:
        import capo_mediaconvert.types.uncompressed_settings

        out["uncompressedSettings"] = (
            capo_mediaconvert.types.uncompressed_settings.serialize_json(
                value["uncompressed_settings"]
            )
        )
    if "vc3_settings" in value:
        import capo_mediaconvert.types.vc3_settings

        out["vc3Settings"] = capo_mediaconvert.types.vc3_settings.serialize_json(
            value["vc3_settings"]
        )
    if "vp8_settings" in value:
        import capo_mediaconvert.types.vp8_settings

        out["vp8Settings"] = capo_mediaconvert.types.vp8_settings.serialize_json(
            value["vp8_settings"]
        )
    if "vp9_settings" in value:
        import capo_mediaconvert.types.vp9_settings

        out["vp9Settings"] = capo_mediaconvert.types.vp9_settings.serialize_json(
            value["vp9_settings"]
        )
    if "xavc_settings" in value:
        import capo_mediaconvert.types.xavc_settings

        out["xavcSettings"] = capo_mediaconvert.types.xavc_settings.serialize_json(
            value["xavc_settings"]
        )
    return out


def deserialize_json(data: dict) -> VideoCodecSettings:
    out: VideoCodecSettings = {}  # type: ignore[typeddict-item]
    if "av1Settings" in data:
        import capo_mediaconvert.types.av1_settings

        out["av1_settings"] = capo_mediaconvert.types.av1_settings.deserialize_json(
            data["av1Settings"]
        )
    if "avcIntraSettings" in data:
        import capo_mediaconvert.types.avc_intra_settings

        out["avc_intra_settings"] = (
            capo_mediaconvert.types.avc_intra_settings.deserialize_json(
                data["avcIntraSettings"]
            )
        )
    if "codec" in data:
        import capo_mediaconvert.types.video_codec

        out["codec"] = capo_mediaconvert.types.video_codec.deserialize_json(
            data["codec"]
        )
    if "frameCaptureSettings" in data:
        import capo_mediaconvert.types.frame_capture_settings

        out["frame_capture_settings"] = (
            capo_mediaconvert.types.frame_capture_settings.deserialize_json(
                data["frameCaptureSettings"]
            )
        )
    if "gifSettings" in data:
        import capo_mediaconvert.types.gif_settings

        out["gif_settings"] = capo_mediaconvert.types.gif_settings.deserialize_json(
            data["gifSettings"]
        )
    if "h264Settings" in data:
        import capo_mediaconvert.types.h264_settings

        out["h264_settings"] = capo_mediaconvert.types.h264_settings.deserialize_json(
            data["h264Settings"]
        )
    if "h265Settings" in data:
        import capo_mediaconvert.types.h265_settings

        out["h265_settings"] = capo_mediaconvert.types.h265_settings.deserialize_json(
            data["h265Settings"]
        )
    if "mpeg2Settings" in data:
        import capo_mediaconvert.types.mpeg2_settings

        out["mpeg2_settings"] = capo_mediaconvert.types.mpeg2_settings.deserialize_json(
            data["mpeg2Settings"]
        )
    if "passthroughSettings" in data:
        import capo_mediaconvert.types.passthrough_settings

        out["passthrough_settings"] = (
            capo_mediaconvert.types.passthrough_settings.deserialize_json(
                data["passthroughSettings"]
            )
        )
    if "proresSettings" in data:
        import capo_mediaconvert.types.prores_settings

        out["prores_settings"] = (
            capo_mediaconvert.types.prores_settings.deserialize_json(
                data["proresSettings"]
            )
        )
    if "uncompressedSettings" in data:
        import capo_mediaconvert.types.uncompressed_settings

        out["uncompressed_settings"] = (
            capo_mediaconvert.types.uncompressed_settings.deserialize_json(
                data["uncompressedSettings"]
            )
        )
    if "vc3Settings" in data:
        import capo_mediaconvert.types.vc3_settings

        out["vc3_settings"] = capo_mediaconvert.types.vc3_settings.deserialize_json(
            data["vc3Settings"]
        )
    if "vp8Settings" in data:
        import capo_mediaconvert.types.vp8_settings

        out["vp8_settings"] = capo_mediaconvert.types.vp8_settings.deserialize_json(
            data["vp8Settings"]
        )
    if "vp9Settings" in data:
        import capo_mediaconvert.types.vp9_settings

        out["vp9_settings"] = capo_mediaconvert.types.vp9_settings.deserialize_json(
            data["vp9Settings"]
        )
    if "xavcSettings" in data:
        import capo_mediaconvert.types.xavc_settings

        out["xavc_settings"] = capo_mediaconvert.types.xavc_settings.deserialize_json(
            data["xavcSettings"]
        )
    return out
