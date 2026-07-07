"""Generated from Smithy shape ``com.amazonaws.medialive#HlsSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.audio_only_hls_settings
    import aws_sdk_medialive.types.fmp4_hls_settings
    import aws_sdk_medialive.types.frame_capture_hls_settings
    import aws_sdk_medialive.types.standard_hls_settings


class HlsSettings(TypedDict, closed=True):
    audio_only_hls_settings: NotRequired[
        "aws_sdk_medialive.types.audio_only_hls_settings.AudioOnlyHlsSettings"
    ]
    fmp4_hls_settings: NotRequired[
        "aws_sdk_medialive.types.fmp4_hls_settings.Fmp4HlsSettings"
    ]
    frame_capture_hls_settings: NotRequired[
        "aws_sdk_medialive.types.frame_capture_hls_settings.FrameCaptureHlsSettings"
    ]
    standard_hls_settings: NotRequired[
        "aws_sdk_medialive.types.standard_hls_settings.StandardHlsSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: HlsSettings) -> dict:
    out: dict = {}
    if "audio_only_hls_settings" in value:
        import aws_sdk_medialive.types.audio_only_hls_settings

        out["audioOnlyHlsSettings"] = (
            aws_sdk_medialive.types.audio_only_hls_settings.serialize_json(
                value["audio_only_hls_settings"]
            )
        )
    if "fmp4_hls_settings" in value:
        import aws_sdk_medialive.types.fmp4_hls_settings

        out["fmp4HlsSettings"] = (
            aws_sdk_medialive.types.fmp4_hls_settings.serialize_json(
                value["fmp4_hls_settings"]
            )
        )
    if "frame_capture_hls_settings" in value:
        import aws_sdk_medialive.types.frame_capture_hls_settings

        out["frameCaptureHlsSettings"] = (
            aws_sdk_medialive.types.frame_capture_hls_settings.serialize_json(
                value["frame_capture_hls_settings"]
            )
        )
    if "standard_hls_settings" in value:
        import aws_sdk_medialive.types.standard_hls_settings

        out["standardHlsSettings"] = (
            aws_sdk_medialive.types.standard_hls_settings.serialize_json(
                value["standard_hls_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> HlsSettings:
    out: HlsSettings = {}  # type: ignore[typeddict-item]
    if "audioOnlyHlsSettings" in data:
        import aws_sdk_medialive.types.audio_only_hls_settings

        out["audio_only_hls_settings"] = (
            aws_sdk_medialive.types.audio_only_hls_settings.deserialize_json(
                data["audioOnlyHlsSettings"]
            )
        )
    if "fmp4HlsSettings" in data:
        import aws_sdk_medialive.types.fmp4_hls_settings

        out["fmp4_hls_settings"] = (
            aws_sdk_medialive.types.fmp4_hls_settings.deserialize_json(
                data["fmp4HlsSettings"]
            )
        )
    if "frameCaptureHlsSettings" in data:
        import aws_sdk_medialive.types.frame_capture_hls_settings

        out["frame_capture_hls_settings"] = (
            aws_sdk_medialive.types.frame_capture_hls_settings.deserialize_json(
                data["frameCaptureHlsSettings"]
            )
        )
    if "standardHlsSettings" in data:
        import aws_sdk_medialive.types.standard_hls_settings

        out["standard_hls_settings"] = (
            aws_sdk_medialive.types.standard_hls_settings.deserialize_json(
                data["standardHlsSettings"]
            )
        )
    return out
