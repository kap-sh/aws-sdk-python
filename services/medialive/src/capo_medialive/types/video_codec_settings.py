"""Generated from Smithy shape ``com.amazonaws.medialive#VideoCodecSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.av1_settings
    import capo_medialive.types.frame_capture_settings
    import capo_medialive.types.h264_settings
    import capo_medialive.types.h265_settings
    import capo_medialive.types.mpeg2_settings


class VideoCodecSettings(TypedDict, closed=True):
    frame_capture_settings: NotRequired[
        "capo_medialive.types.frame_capture_settings.FrameCaptureSettings"
    ]
    h264_settings: NotRequired["capo_medialive.types.h264_settings.H264Settings"]
    h265_settings: NotRequired["capo_medialive.types.h265_settings.H265Settings"]
    mpeg2_settings: NotRequired["capo_medialive.types.mpeg2_settings.Mpeg2Settings"]
    av1_settings: NotRequired["capo_medialive.types.av1_settings.Av1Settings"]


# --- restJson1 ser/de ---
def serialize_json(value: VideoCodecSettings) -> dict:
    out: dict = {}
    if "frame_capture_settings" in value:
        import capo_medialive.types.frame_capture_settings

        out["frameCaptureSettings"] = (
            capo_medialive.types.frame_capture_settings.serialize_json(
                value["frame_capture_settings"]
            )
        )
    if "h264_settings" in value:
        import capo_medialive.types.h264_settings

        out["h264Settings"] = capo_medialive.types.h264_settings.serialize_json(
            value["h264_settings"]
        )
    if "h265_settings" in value:
        import capo_medialive.types.h265_settings

        out["h265Settings"] = capo_medialive.types.h265_settings.serialize_json(
            value["h265_settings"]
        )
    if "mpeg2_settings" in value:
        import capo_medialive.types.mpeg2_settings

        out["mpeg2Settings"] = capo_medialive.types.mpeg2_settings.serialize_json(
            value["mpeg2_settings"]
        )
    if "av1_settings" in value:
        import capo_medialive.types.av1_settings

        out["av1Settings"] = capo_medialive.types.av1_settings.serialize_json(
            value["av1_settings"]
        )
    return out


def deserialize_json(data: dict) -> VideoCodecSettings:
    out: VideoCodecSettings = {}  # type: ignore[typeddict-item]
    if "frameCaptureSettings" in data:
        import capo_medialive.types.frame_capture_settings

        out["frame_capture_settings"] = (
            capo_medialive.types.frame_capture_settings.deserialize_json(
                data["frameCaptureSettings"]
            )
        )
    if "h264Settings" in data:
        import capo_medialive.types.h264_settings

        out["h264_settings"] = capo_medialive.types.h264_settings.deserialize_json(
            data["h264Settings"]
        )
    if "h265Settings" in data:
        import capo_medialive.types.h265_settings

        out["h265_settings"] = capo_medialive.types.h265_settings.deserialize_json(
            data["h265Settings"]
        )
    if "mpeg2Settings" in data:
        import capo_medialive.types.mpeg2_settings

        out["mpeg2_settings"] = capo_medialive.types.mpeg2_settings.deserialize_json(
            data["mpeg2Settings"]
        )
    if "av1Settings" in data:
        import capo_medialive.types.av1_settings

        out["av1_settings"] = capo_medialive.types.av1_settings.deserialize_json(
            data["av1Settings"]
        )
    return out
