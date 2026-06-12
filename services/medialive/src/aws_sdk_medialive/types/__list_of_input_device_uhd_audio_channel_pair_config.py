"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfInputDeviceUhdAudioChannelPairConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.input_device_uhd_audio_channel_pair_config

__listOfInputDeviceUhdAudioChannelPairConfig: TypeAlias = list[
    "aws_sdk_medialive.types.input_device_uhd_audio_channel_pair_config.InputDeviceUhdAudioChannelPairConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInputDeviceUhdAudioChannelPairConfig) -> list:
    import aws_sdk_medialive.types.input_device_uhd_audio_channel_pair_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medialive.types.input_device_uhd_audio_channel_pair_config.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfInputDeviceUhdAudioChannelPairConfig:
    import aws_sdk_medialive.types.input_device_uhd_audio_channel_pair_config

    out: __listOfInputDeviceUhdAudioChannelPairConfig = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.input_device_uhd_audio_channel_pair_config.deserialize_json(
                item
            )
        )
    return out
