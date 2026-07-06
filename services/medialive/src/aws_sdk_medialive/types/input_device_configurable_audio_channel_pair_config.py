"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceConfigurableAudioChannelPairConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer
    import aws_sdk_medialive.types.input_device_configurable_audio_channel_pair_profile


class InputDeviceConfigurableAudioChannelPairConfig(TypedDict, closed=True):
    id: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    """The ID for one audio pair configuration, a value from 1 to 8."""
    profile: NotRequired[
        "aws_sdk_medialive.types.input_device_configurable_audio_channel_pair_profile.InputDeviceConfigurableAudioChannelPairProfile"
    ]
    """The profile to set for one audio pair configuration. Choose an enumeration value. Each value describes one audio configuration using the format (rate control algorithm)-(codec)_(quality)-(bitrate in bytes). For example, CBR-AAC_HQ-192000. Or choose DISABLED, in which case the device won't produce audio for this pair."""


# --- restJson1 ser/de ---
def serialize_json(value: InputDeviceConfigurableAudioChannelPairConfig) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "profile" in value:
        import aws_sdk_medialive.types.input_device_configurable_audio_channel_pair_profile

        out["profile"] = (
            aws_sdk_medialive.types.input_device_configurable_audio_channel_pair_profile.serialize_json(
                value["profile"]
            )
        )
    return out


def deserialize_json(data: dict) -> InputDeviceConfigurableAudioChannelPairConfig:
    out: InputDeviceConfigurableAudioChannelPairConfig = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "profile" in data:
        import aws_sdk_medialive.types.input_device_configurable_audio_channel_pair_profile

        out["profile"] = (
            aws_sdk_medialive.types.input_device_configurable_audio_channel_pair_profile.deserialize_json(
                data["profile"]
            )
        )
    return out
