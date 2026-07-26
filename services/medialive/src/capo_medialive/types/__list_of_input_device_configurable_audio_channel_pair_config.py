"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfInputDeviceConfigurableAudioChannelPairConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.input_device_configurable_audio_channel_pair_config

__listOfInputDeviceConfigurableAudioChannelPairConfig: TypeAlias = list[
    "capo_medialive.types.input_device_configurable_audio_channel_pair_config.InputDeviceConfigurableAudioChannelPairConfig"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: __listOfInputDeviceConfigurableAudioChannelPairConfig,
) -> list:
    import capo_medialive.types.input_device_configurable_audio_channel_pair_config

    out: list = []
    for item in value:
        out.append(
            capo_medialive.types.input_device_configurable_audio_channel_pair_config.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> __listOfInputDeviceConfigurableAudioChannelPairConfig:
    import capo_medialive.types.input_device_configurable_audio_channel_pair_config

    out: __listOfInputDeviceConfigurableAudioChannelPairConfig = []
    for item in data:
        out.append(
            capo_medialive.types.input_device_configurable_audio_channel_pair_config.deserialize_json(
                item
            )
        )
    return out
