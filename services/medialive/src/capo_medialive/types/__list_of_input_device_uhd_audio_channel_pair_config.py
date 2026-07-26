"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfInputDeviceUhdAudioChannelPairConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.input_device_uhd_audio_channel_pair_config

__listOfInputDeviceUhdAudioChannelPairConfig: TypeAlias = list[
    "capo_medialive.types.input_device_uhd_audio_channel_pair_config.InputDeviceUhdAudioChannelPairConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInputDeviceUhdAudioChannelPairConfig) -> list:
    import capo_medialive.types.input_device_uhd_audio_channel_pair_config

    out: list = []
    for item in value:
        out.append(
            capo_medialive.types.input_device_uhd_audio_channel_pair_config.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfInputDeviceUhdAudioChannelPairConfig:
    import capo_medialive.types.input_device_uhd_audio_channel_pair_config

    out: __listOfInputDeviceUhdAudioChannelPairConfig = []
    for item in data:
        out.append(
            capo_medialive.types.input_device_uhd_audio_channel_pair_config.deserialize_json(
                item
            )
        )
    return out
