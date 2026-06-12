"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceUhdSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__double
    import aws_sdk_medialive.types.__integer
    import aws_sdk_medialive.types.__list_of_input_device_uhd_audio_channel_pair_config
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.input_device_active_input
    import aws_sdk_medialive.types.input_device_codec
    import aws_sdk_medialive.types.input_device_configured_input
    import aws_sdk_medialive.types.input_device_media_connect_settings
    import aws_sdk_medialive.types.input_device_scan_type
    import aws_sdk_medialive.types.input_device_state


class InputDeviceUhdSettings(TypedDict):
    active_input: NotRequired[
        "aws_sdk_medialive.types.input_device_active_input.InputDeviceActiveInput"
    ]
    """If you specified Auto as the configured input, specifies which of the sources is currently active (SDI or HDMI)."""
    configured_input: NotRequired[
        "aws_sdk_medialive.types.input_device_configured_input.InputDeviceConfiguredInput"
    ]
    """The source at the input device that is currently active. You can specify this source."""
    device_state: NotRequired[
        "aws_sdk_medialive.types.input_device_state.InputDeviceState"
    ]
    """The state of the input device."""
    framerate: NotRequired["aws_sdk_medialive.types.__double.__double"]
    """The frame rate of the video source."""
    height: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    """The height of the video source, in pixels."""
    max_bitrate: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    """The current maximum bitrate for ingesting this source, in bits per second. You can specify this maximum."""
    scan_type: NotRequired[
        "aws_sdk_medialive.types.input_device_scan_type.InputDeviceScanType"
    ]
    """The scan type of the video source."""
    width: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    """The width of the video source, in pixels."""
    latency_ms: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    """The Link device's buffer size (latency) in milliseconds (ms). You can specify this value."""
    codec: NotRequired["aws_sdk_medialive.types.input_device_codec.InputDeviceCodec"]
    """The codec for the video that the device produces."""
    mediaconnect_settings: NotRequired[
        "aws_sdk_medialive.types.input_device_media_connect_settings.InputDeviceMediaConnectSettings"
    ]
    """Information about the MediaConnect flow attached to the device. Returned only if the outputType is MEDIACONNECT_FLOW."""
    audio_channel_pairs: NotRequired[
        "aws_sdk_medialive.types.__list_of_input_device_uhd_audio_channel_pair_config.__listOfInputDeviceUhdAudioChannelPairConfig"
    ]
    """An array of eight audio configurations, one for each audio pair in the source. Each audio configuration specifies either to exclude the pair, or to format it and include it in the output from the UHD device. Applies only when the device is configured as the source for a MediaConnect flow."""
    input_resolution: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The resolution of the Link device's source (HD or UHD). This value determines MediaLive resource allocation and billing for this input."""


# --- restJson1 ser/de ---
def serialize_json(value: InputDeviceUhdSettings) -> dict:
    out: dict = {}
    if "active_input" in value:
        import aws_sdk_medialive.types.input_device_active_input

        out["activeInput"] = (
            aws_sdk_medialive.types.input_device_active_input.serialize_json(
                value["active_input"]
            )
        )
    if "configured_input" in value:
        import aws_sdk_medialive.types.input_device_configured_input

        out["configuredInput"] = (
            aws_sdk_medialive.types.input_device_configured_input.serialize_json(
                value["configured_input"]
            )
        )
    if "device_state" in value:
        import aws_sdk_medialive.types.input_device_state

        out["deviceState"] = aws_sdk_medialive.types.input_device_state.serialize_json(
            value["device_state"]
        )
    if "framerate" in value:
        out["framerate"] = value["framerate"]
    if "height" in value:
        out["height"] = value["height"]
    if "max_bitrate" in value:
        out["maxBitrate"] = value["max_bitrate"]
    if "scan_type" in value:
        import aws_sdk_medialive.types.input_device_scan_type

        out["scanType"] = aws_sdk_medialive.types.input_device_scan_type.serialize_json(
            value["scan_type"]
        )
    if "width" in value:
        out["width"] = value["width"]
    if "latency_ms" in value:
        out["latencyMs"] = value["latency_ms"]
    if "codec" in value:
        import aws_sdk_medialive.types.input_device_codec

        out["codec"] = aws_sdk_medialive.types.input_device_codec.serialize_json(
            value["codec"]
        )
    if "mediaconnect_settings" in value:
        import aws_sdk_medialive.types.input_device_media_connect_settings

        out["mediaconnectSettings"] = (
            aws_sdk_medialive.types.input_device_media_connect_settings.serialize_json(
                value["mediaconnect_settings"]
            )
        )
    if "audio_channel_pairs" in value:
        import aws_sdk_medialive.types.__list_of_input_device_uhd_audio_channel_pair_config

        out["audioChannelPairs"] = (
            aws_sdk_medialive.types.__list_of_input_device_uhd_audio_channel_pair_config.serialize_json(
                value["audio_channel_pairs"]
            )
        )
    if "input_resolution" in value:
        out["inputResolution"] = value["input_resolution"]
    return out


def deserialize_json(data: dict) -> InputDeviceUhdSettings:
    out: InputDeviceUhdSettings = {}  # type: ignore[typeddict-item]
    if "activeInput" in data:
        import aws_sdk_medialive.types.input_device_active_input

        out["active_input"] = (
            aws_sdk_medialive.types.input_device_active_input.deserialize_json(
                data["activeInput"]
            )
        )
    if "configuredInput" in data:
        import aws_sdk_medialive.types.input_device_configured_input

        out["configured_input"] = (
            aws_sdk_medialive.types.input_device_configured_input.deserialize_json(
                data["configuredInput"]
            )
        )
    if "deviceState" in data:
        import aws_sdk_medialive.types.input_device_state

        out["device_state"] = (
            aws_sdk_medialive.types.input_device_state.deserialize_json(
                data["deviceState"]
            )
        )
    if "framerate" in data:
        out["framerate"] = data["framerate"]
    if "height" in data:
        out["height"] = data["height"]
    if "maxBitrate" in data:
        out["max_bitrate"] = data["maxBitrate"]
    if "scanType" in data:
        import aws_sdk_medialive.types.input_device_scan_type

        out["scan_type"] = (
            aws_sdk_medialive.types.input_device_scan_type.deserialize_json(
                data["scanType"]
            )
        )
    if "width" in data:
        out["width"] = data["width"]
    if "latencyMs" in data:
        out["latency_ms"] = data["latencyMs"]
    if "codec" in data:
        import aws_sdk_medialive.types.input_device_codec

        out["codec"] = aws_sdk_medialive.types.input_device_codec.deserialize_json(
            data["codec"]
        )
    if "mediaconnectSettings" in data:
        import aws_sdk_medialive.types.input_device_media_connect_settings

        out["mediaconnect_settings"] = (
            aws_sdk_medialive.types.input_device_media_connect_settings.deserialize_json(
                data["mediaconnectSettings"]
            )
        )
    if "audioChannelPairs" in data:
        import aws_sdk_medialive.types.__list_of_input_device_uhd_audio_channel_pair_config

        out["audio_channel_pairs"] = (
            aws_sdk_medialive.types.__list_of_input_device_uhd_audio_channel_pair_config.deserialize_json(
                data["audioChannelPairs"]
            )
        )
    if "inputResolution" in data:
        out["input_resolution"] = data["inputResolution"]
    return out
