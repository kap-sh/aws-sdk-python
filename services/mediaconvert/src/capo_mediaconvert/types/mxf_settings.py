"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MxfSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.mxf_afd_signaling
    import capo_mediaconvert.types.mxf_profile
    import capo_mediaconvert.types.mxf_uncompressed_audio_wrapping
    import capo_mediaconvert.types.mxf_xavc_profile_settings


class MxfSettings(TypedDict, closed=True):
    afd_signaling: NotRequired[
        "capo_mediaconvert.types.mxf_afd_signaling.MxfAfdSignaling"
    ]
    """Optional. When you have AFD signaling set up in your output video stream, use this setting to choose whether to also include it in the MXF wrapper. Choose Don't copy to exclude AFD signaling from the MXF wrapper. Choose Copy from video stream to copy the AFD values from the video stream for this output to the MXF wrapper. Regardless of which option you choose, the AFD values remain in the video stream. Related settings: To set up your output to include or exclude AFD values, see AfdSignaling, under VideoDescription. On the console, find AFD signaling under the output's video encoding settings."""
    profile: NotRequired["capo_mediaconvert.types.mxf_profile.MxfProfile"]
    """Specify the MXF profile, also called shim, for this output. To automatically select a profile according to your output video codec and resolution, leave blank. For a list of codecs supported with each MXF profile, see https://docs.aws.amazon.com/mediaconvert/latest/ug/codecs-supported-with-each-mxf-profile.html. For more information about the automatic selection behavior, see https://docs.aws.amazon.com/mediaconvert/latest/ug/default-automatic-selection-of-mxf-profiles.html."""
    uncompressed_audio_wrapping: NotRequired[
        "capo_mediaconvert.types.mxf_uncompressed_audio_wrapping.MxfUncompressedAudioWrapping"
    ]
    """Choose the audio frame wrapping mode for PCM tracks in MXF outputs. AUTO (default): Uses codec-appropriate defaults - BWF for H.264/AVC, AES3 for MPEG2/XDCAM. AES3: Use AES3 frame wrapping with SMPTE-compliant descriptors. This setting only takes effect when the MXF profile is OP1a."""
    xavc_profile_settings: NotRequired[
        "capo_mediaconvert.types.mxf_xavc_profile_settings.MxfXavcProfileSettings"
    ]
    """Specify the XAVC profile settings for MXF outputs when you set your MXF profile to XAVC."""


# --- restJson1 ser/de ---
def serialize_json(value: MxfSettings) -> dict:
    out: dict = {}
    if "afd_signaling" in value:
        import capo_mediaconvert.types.mxf_afd_signaling

        out["afdSignaling"] = capo_mediaconvert.types.mxf_afd_signaling.serialize_json(
            value["afd_signaling"]
        )
    if "profile" in value:
        import capo_mediaconvert.types.mxf_profile

        out["profile"] = capo_mediaconvert.types.mxf_profile.serialize_json(
            value["profile"]
        )
    if "uncompressed_audio_wrapping" in value:
        import capo_mediaconvert.types.mxf_uncompressed_audio_wrapping

        out["uncompressedAudioWrapping"] = (
            capo_mediaconvert.types.mxf_uncompressed_audio_wrapping.serialize_json(
                value["uncompressed_audio_wrapping"]
            )
        )
    if "xavc_profile_settings" in value:
        import capo_mediaconvert.types.mxf_xavc_profile_settings

        out["xavcProfileSettings"] = (
            capo_mediaconvert.types.mxf_xavc_profile_settings.serialize_json(
                value["xavc_profile_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> MxfSettings:
    out: MxfSettings = {}  # type: ignore[typeddict-item]
    if "afdSignaling" in data:
        import capo_mediaconvert.types.mxf_afd_signaling

        out["afd_signaling"] = (
            capo_mediaconvert.types.mxf_afd_signaling.deserialize_json(
                data["afdSignaling"]
            )
        )
    if "profile" in data:
        import capo_mediaconvert.types.mxf_profile

        out["profile"] = capo_mediaconvert.types.mxf_profile.deserialize_json(
            data["profile"]
        )
    if "uncompressedAudioWrapping" in data:
        import capo_mediaconvert.types.mxf_uncompressed_audio_wrapping

        out["uncompressed_audio_wrapping"] = (
            capo_mediaconvert.types.mxf_uncompressed_audio_wrapping.deserialize_json(
                data["uncompressedAudioWrapping"]
            )
        )
    if "xavcProfileSettings" in data:
        import capo_mediaconvert.types.mxf_xavc_profile_settings

        out["xavc_profile_settings"] = (
            capo_mediaconvert.types.mxf_xavc_profile_settings.deserialize_json(
                data["xavcProfileSettings"]
            )
        )
    return out
