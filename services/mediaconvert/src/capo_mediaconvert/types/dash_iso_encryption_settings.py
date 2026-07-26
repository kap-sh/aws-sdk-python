"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DashIsoEncryptionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.dash_iso_playback_device_compatibility
    import capo_mediaconvert.types.speke_key_provider


class DashIsoEncryptionSettings(TypedDict, closed=True):
    playback_device_compatibility: NotRequired[
        "capo_mediaconvert.types.dash_iso_playback_device_compatibility.DashIsoPlaybackDeviceCompatibility"
    ]
    """This setting can improve the compatibility of your output with video players on obsolete devices. It applies only to DASH H.264 outputs with DRM encryption. Choose Unencrypted SEI only to correct problems with playback on older devices. Otherwise, keep the default setting CENC v1. If you choose Unencrypted SEI, for that output, the service will exclude the access unit delimiter and will leave the SEI NAL units unencrypted."""
    speke_key_provider: NotRequired[
        "capo_mediaconvert.types.speke_key_provider.SpekeKeyProvider"
    ]
    """If your output group type is HLS, DASH, or Microsoft Smooth, use these settings when doing DRM encryption with a SPEKE-compliant key provider. If your output group type is CMAF, use the SpekeKeyProviderCmaf settings instead."""


# --- restJson1 ser/de ---
def serialize_json(value: DashIsoEncryptionSettings) -> dict:
    out: dict = {}
    if "playback_device_compatibility" in value:
        import capo_mediaconvert.types.dash_iso_playback_device_compatibility

        out["playbackDeviceCompatibility"] = (
            capo_mediaconvert.types.dash_iso_playback_device_compatibility.serialize_json(
                value["playback_device_compatibility"]
            )
        )
    if "speke_key_provider" in value:
        import capo_mediaconvert.types.speke_key_provider

        out["spekeKeyProvider"] = (
            capo_mediaconvert.types.speke_key_provider.serialize_json(
                value["speke_key_provider"]
            )
        )
    return out


def deserialize_json(data: dict) -> DashIsoEncryptionSettings:
    out: DashIsoEncryptionSettings = {}  # type: ignore[typeddict-item]
    if "playbackDeviceCompatibility" in data:
        import capo_mediaconvert.types.dash_iso_playback_device_compatibility

        out["playback_device_compatibility"] = (
            capo_mediaconvert.types.dash_iso_playback_device_compatibility.deserialize_json(
                data["playbackDeviceCompatibility"]
            )
        )
    if "spekeKeyProvider" in data:
        import capo_mediaconvert.types.speke_key_provider

        out["speke_key_provider"] = (
            capo_mediaconvert.types.speke_key_provider.deserialize_json(
                data["spekeKeyProvider"]
            )
        )
    return out
