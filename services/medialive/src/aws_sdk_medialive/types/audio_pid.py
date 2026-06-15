"""Generated from Smithy shape ``com.amazonaws.medialive#AudioPid``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min0_max8191
    import aws_sdk_medialive.types.audio_dolby_e_decode
    import aws_sdk_medialive.types.audio_pre_mixer_settings


class AudioPid(TypedDict):
    dolby_e_decode: NotRequired[
        "aws_sdk_medialive.types.audio_dolby_e_decode.AudioDolbyEDecode"
    ]
    r"""Configure decoding options for Dolby E streams - these should be Dolby E frames carried in PCM streams tagged with SMPTE-337. When using the 'pids' array, if this field is not specified and Dolby E content is present, the decoder will extract the specified program. To maintain legacy behavior (allPrograms), explicitly set programSelection to \"allChannels\"."""
    pid: NotRequired[
        "aws_sdk_medialive.types.__integer_min0_max8191.__integerMin0Max8191"
    ]
    """PID value from within a source."""
    premix_settings: NotRequired[
        "aws_sdk_medialive.types.audio_pre_mixer_settings.AudioPreMixerSettings"
    ]
    """Optional audio pre-mixer settings for this PID. When specified, allows per-PID audio processing including channel remixing, gain adjustment, and loudness normalization before interleaving."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioPid) -> dict:
    out: dict = {}
    if "dolby_e_decode" in value:
        import aws_sdk_medialive.types.audio_dolby_e_decode

        out["dolbyEDecode"] = (
            aws_sdk_medialive.types.audio_dolby_e_decode.serialize_json(
                value["dolby_e_decode"]
            )
        )
    if "pid" in value:
        out["pid"] = value["pid"]
    if "premix_settings" in value:
        import aws_sdk_medialive.types.audio_pre_mixer_settings

        out["premixSettings"] = (
            aws_sdk_medialive.types.audio_pre_mixer_settings.serialize_json(
                value["premix_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioPid:
    out: AudioPid = {}  # type: ignore[typeddict-item]
    if "dolbyEDecode" in data:
        import aws_sdk_medialive.types.audio_dolby_e_decode

        out["dolby_e_decode"] = (
            aws_sdk_medialive.types.audio_dolby_e_decode.deserialize_json(
                data["dolbyEDecode"]
            )
        )
    if "pid" in data:
        out["pid"] = data["pid"]
    if "premixSettings" in data:
        import aws_sdk_medialive.types.audio_pre_mixer_settings

        out["premix_settings"] = (
            aws_sdk_medialive.types.audio_pre_mixer_settings.deserialize_json(
                data["premixSettings"]
            )
        )
    return out
