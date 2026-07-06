"""Generated from Smithy shape ``com.amazonaws.medialive#FrameCaptureCdnSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.frame_capture_s3_settings


class FrameCaptureCdnSettings(TypedDict, closed=True):
    frame_capture_s3_settings: NotRequired[
        "aws_sdk_medialive.types.frame_capture_s3_settings.FrameCaptureS3Settings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: FrameCaptureCdnSettings) -> dict:
    out: dict = {}
    if "frame_capture_s3_settings" in value:
        import aws_sdk_medialive.types.frame_capture_s3_settings

        out["frameCaptureS3Settings"] = (
            aws_sdk_medialive.types.frame_capture_s3_settings.serialize_json(
                value["frame_capture_s3_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> FrameCaptureCdnSettings:
    out: FrameCaptureCdnSettings = {}  # type: ignore[typeddict-item]
    if "frameCaptureS3Settings" in data:
        import aws_sdk_medialive.types.frame_capture_s3_settings

        out["frame_capture_s3_settings"] = (
            aws_sdk_medialive.types.frame_capture_s3_settings.deserialize_json(
                data["frameCaptureS3Settings"]
            )
        )
    return out
