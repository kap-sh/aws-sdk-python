"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceConfigurableSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer
    import aws_sdk_medialive.types.__list_of_input_device_configurable_audio_channel_pair_config
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.input_device_codec
    import aws_sdk_medialive.types.input_device_configured_input
    import aws_sdk_medialive.types.input_device_media_connect_configurable_settings


class InputDeviceConfigurableSettings(TypedDict, closed=True):
    configured_input: NotRequired[
        "aws_sdk_medialive.types.input_device_configured_input.InputDeviceConfiguredInput"
    ]
    """The input source that you want to use. If the device has a source connected to only one of its input ports, or if you don't care which source the device sends, specify Auto. If the device has sources connected to both its input ports, and you want to use a specific source, specify the source."""
    max_bitrate: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    """The maximum bitrate in bits per second. Set a value here to throttle the bitrate of the source video."""
    latency_ms: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    """The Link device's buffer size (latency) in milliseconds (ms)."""
    codec: NotRequired["aws_sdk_medialive.types.input_device_codec.InputDeviceCodec"]
    """Choose the codec for the video that the device produces. Only UHD devices can specify this parameter."""
    mediaconnect_settings: NotRequired[
        "aws_sdk_medialive.types.input_device_media_connect_configurable_settings.InputDeviceMediaConnectConfigurableSettings"
    ]
    """To attach this device to a MediaConnect flow, specify these parameters. To detach an existing flow, enter {} for the value of mediaconnectSettings. Only UHD devices can specify this parameter."""
    audio_channel_pairs: NotRequired[
        "aws_sdk_medialive.types.__list_of_input_device_configurable_audio_channel_pair_config.__listOfInputDeviceConfigurableAudioChannelPairConfig"
    ]
    """An array of eight audio configurations, one for each audio pair in the source. Set up each audio configuration either to exclude the pair, or to format it and include it in the output from the device. This parameter applies only to UHD devices, and only when the device is configured as the source for a MediaConnect flow. For an HD device, you configure the audio by setting up audio selectors in the channel configuration."""
    input_resolution: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Choose the resolution of the Link device's source (HD or UHD). Make sure the resolution matches the current source from the device. This value determines MediaLive resource allocation and billing for this input. Only UHD devices can specify this parameter."""


# --- restJson1 ser/de ---
def serialize_json(value: InputDeviceConfigurableSettings) -> dict:
    out: dict = {}
    if "configured_input" in value:
        import aws_sdk_medialive.types.input_device_configured_input

        out["configuredInput"] = (
            aws_sdk_medialive.types.input_device_configured_input.serialize_json(
                value["configured_input"]
            )
        )
    if "max_bitrate" in value:
        out["maxBitrate"] = value["max_bitrate"]
    if "latency_ms" in value:
        out["latencyMs"] = value["latency_ms"]
    if "codec" in value:
        import aws_sdk_medialive.types.input_device_codec

        out["codec"] = aws_sdk_medialive.types.input_device_codec.serialize_json(
            value["codec"]
        )
    if "mediaconnect_settings" in value:
        import aws_sdk_medialive.types.input_device_media_connect_configurable_settings

        out["mediaconnectSettings"] = (
            aws_sdk_medialive.types.input_device_media_connect_configurable_settings.serialize_json(
                value["mediaconnect_settings"]
            )
        )
    if "audio_channel_pairs" in value:
        import aws_sdk_medialive.types.__list_of_input_device_configurable_audio_channel_pair_config

        out["audioChannelPairs"] = (
            aws_sdk_medialive.types.__list_of_input_device_configurable_audio_channel_pair_config.serialize_json(
                value["audio_channel_pairs"]
            )
        )
    if "input_resolution" in value:
        out["inputResolution"] = value["input_resolution"]
    return out


def deserialize_json(data: dict) -> InputDeviceConfigurableSettings:
    out: InputDeviceConfigurableSettings = {}  # type: ignore[typeddict-item]
    if "configuredInput" in data:
        import aws_sdk_medialive.types.input_device_configured_input

        out["configured_input"] = (
            aws_sdk_medialive.types.input_device_configured_input.deserialize_json(
                data["configuredInput"]
            )
        )
    if "maxBitrate" in data:
        out["max_bitrate"] = data["maxBitrate"]
    if "latencyMs" in data:
        out["latency_ms"] = data["latencyMs"]
    if "codec" in data:
        import aws_sdk_medialive.types.input_device_codec

        out["codec"] = aws_sdk_medialive.types.input_device_codec.deserialize_json(
            data["codec"]
        )
    if "mediaconnectSettings" in data:
        import aws_sdk_medialive.types.input_device_media_connect_configurable_settings

        out["mediaconnect_settings"] = (
            aws_sdk_medialive.types.input_device_media_connect_configurable_settings.deserialize_json(
                data["mediaconnectSettings"]
            )
        )
    if "audioChannelPairs" in data:
        import aws_sdk_medialive.types.__list_of_input_device_configurable_audio_channel_pair_config

        out["audio_channel_pairs"] = (
            aws_sdk_medialive.types.__list_of_input_device_configurable_audio_channel_pair_config.deserialize_json(
                data["audioChannelPairs"]
            )
        )
    if "inputResolution" in data:
        out["input_resolution"] = data["inputResolution"]
    return out
