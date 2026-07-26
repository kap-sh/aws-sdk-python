"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceUhdAudioChannelPairConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer
    import capo_medialive.types.input_device_uhd_audio_channel_pair_profile


class InputDeviceUhdAudioChannelPairConfig(TypedDict, closed=True):
    id: NotRequired["capo_medialive.types.__integer.__integer"]
    """The ID for one audio pair configuration, a value from 1 to 8."""
    profile: NotRequired[
        "capo_medialive.types.input_device_uhd_audio_channel_pair_profile.InputDeviceUhdAudioChannelPairProfile"
    ]
    """The profile for one audio pair configuration. This property describes one audio configuration in the format (rate control algorithm)-(codec)_(quality)-(bitrate in bytes). For example, CBR-AAC_HQ-192000. Or DISABLED, in which case the device won't produce audio for this pair."""


# --- restJson1 ser/de ---
def serialize_json(value: InputDeviceUhdAudioChannelPairConfig) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "profile" in value:
        import capo_medialive.types.input_device_uhd_audio_channel_pair_profile

        out["profile"] = (
            capo_medialive.types.input_device_uhd_audio_channel_pair_profile.serialize_json(
                value["profile"]
            )
        )
    return out


def deserialize_json(data: dict) -> InputDeviceUhdAudioChannelPairConfig:
    out: InputDeviceUhdAudioChannelPairConfig = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "profile" in data:
        import capo_medialive.types.input_device_uhd_audio_channel_pair_profile

        out["profile"] = (
            capo_medialive.types.input_device_uhd_audio_channel_pair_profile.deserialize_json(
                data["profile"]
            )
        )
    return out
