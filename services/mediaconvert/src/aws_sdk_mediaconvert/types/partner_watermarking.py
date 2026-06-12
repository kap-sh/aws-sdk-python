"""Generated from Smithy shape ``com.amazonaws.mediaconvert#PartnerWatermarking``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.nex_guard_file_marker_settings


class PartnerWatermarking(TypedDict):
    nexguard_file_marker_settings: NotRequired[
        "aws_sdk_mediaconvert.types.nex_guard_file_marker_settings.NexGuardFileMarkerSettings"
    ]
    """For forensic video watermarking, MediaConvert supports Nagra NexGuard File Marker watermarking. MediaConvert supports both PreRelease Content (NGPR/G2) and OTT Streaming workflows."""


# --- restJson1 ser/de ---
def serialize_json(value: PartnerWatermarking) -> dict:
    out: dict = {}
    if "nexguard_file_marker_settings" in value:
        import aws_sdk_mediaconvert.types.nex_guard_file_marker_settings

        out["nexguardFileMarkerSettings"] = (
            aws_sdk_mediaconvert.types.nex_guard_file_marker_settings.serialize_json(
                value["nexguard_file_marker_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> PartnerWatermarking:
    out: PartnerWatermarking = {}  # type: ignore[typeddict-item]
    if "nexguardFileMarkerSettings" in data:
        import aws_sdk_mediaconvert.types.nex_guard_file_marker_settings

        out["nexguard_file_marker_settings"] = (
            aws_sdk_mediaconvert.types.nex_guard_file_marker_settings.deserialize_json(
                data["nexguardFileMarkerSettings"]
            )
        )
    return out
