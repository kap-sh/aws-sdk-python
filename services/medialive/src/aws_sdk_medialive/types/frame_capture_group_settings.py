"""Generated from Smithy shape ``com.amazonaws.medialive#FrameCaptureGroupSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.frame_capture_cdn_settings
    import aws_sdk_medialive.types.output_location_ref


class FrameCaptureGroupSettings(TypedDict):
    destination: NotRequired[
        "aws_sdk_medialive.types.output_location_ref.OutputLocationRef"
    ]
    r"""The destination for the frame capture files. Either the URI for an Amazon S3 bucket and object, plus a file name prefix (for example, s3ssl://sportsDelivery/highlights/20180820/curling-) or the URI for a MediaStore container, plus a file name prefix (for example, mediastoressl://sportsDelivery/20180820/curling-). The final file names consist of the prefix from the destination field (for example, \"curling-\") + name modifier + the counter (5 digits, starting from 00001) + extension (which is always .jpg). For example, curling-low.00001.jpg"""
    frame_capture_cdn_settings: NotRequired[
        "aws_sdk_medialive.types.frame_capture_cdn_settings.FrameCaptureCdnSettings"
    ]
    """Parameters that control interactions with the CDN."""


# --- restJson1 ser/de ---
def serialize_json(value: FrameCaptureGroupSettings) -> dict:
    out: dict = {}
    if "destination" in value:
        import aws_sdk_medialive.types.output_location_ref

        out["destination"] = aws_sdk_medialive.types.output_location_ref.serialize_json(
            value["destination"]
        )
    if "frame_capture_cdn_settings" in value:
        import aws_sdk_medialive.types.frame_capture_cdn_settings

        out["frameCaptureCdnSettings"] = (
            aws_sdk_medialive.types.frame_capture_cdn_settings.serialize_json(
                value["frame_capture_cdn_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> FrameCaptureGroupSettings:
    out: FrameCaptureGroupSettings = {}  # type: ignore[typeddict-item]
    if "destination" in data:
        import aws_sdk_medialive.types.output_location_ref

        out["destination"] = (
            aws_sdk_medialive.types.output_location_ref.deserialize_json(
                data["destination"]
            )
        )
    if "frameCaptureCdnSettings" in data:
        import aws_sdk_medialive.types.frame_capture_cdn_settings

        out["frame_capture_cdn_settings"] = (
            aws_sdk_medialive.types.frame_capture_cdn_settings.deserialize_json(
                data["frameCaptureCdnSettings"]
            )
        )
    return out
