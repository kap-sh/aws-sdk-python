"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceUhdSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__double
    import capo_medialive.types.__integer
    import capo_medialive.types.__list_of_input_device_uhd_audio_channel_pair_config
    import capo_medialive.types.__string
    import capo_medialive.types.input_device_active_input
    import capo_medialive.types.input_device_codec
    import capo_medialive.types.input_device_configured_input
    import capo_medialive.types.input_device_media_connect_settings
    import capo_medialive.types.input_device_scan_type
    import capo_medialive.types.input_device_state


class InputDeviceUhdSettings(TypedDict, closed=True):
    active_input: NotRequired[
        "capo_medialive.types.input_device_active_input.InputDeviceActiveInput"
    ]
    """If you specified Auto as the configured input, specifies which of the sources is currently active (SDI or HDMI)."""
    configured_input: NotRequired[
        "capo_medialive.types.input_device_configured_input.InputDeviceConfiguredInput"
    ]
    """The source at the input device that is currently active. You can specify this source."""
    device_state: NotRequired[
        "capo_medialive.types.input_device_state.InputDeviceState"
    ]
    """The state of the input device."""
    framerate: NotRequired["capo_medialive.types.__double.__double"]
    """The frame rate of the video source."""
    height: NotRequired["capo_medialive.types.__integer.__integer"]
    """The height of the video source, in pixels."""
    max_bitrate: NotRequired["capo_medialive.types.__integer.__integer"]
    """The current maximum bitrate for ingesting this source, in bits per second. You can specify this maximum."""
    scan_type: NotRequired[
        "capo_medialive.types.input_device_scan_type.InputDeviceScanType"
    ]
    """The scan type of the video source."""
    width: NotRequired["capo_medialive.types.__integer.__integer"]
    """The width of the video source, in pixels."""
    latency_ms: NotRequired["capo_medialive.types.__integer.__integer"]
    """The Link device's buffer size (latency) in milliseconds (ms). You can specify this value."""
    codec: NotRequired["capo_medialive.types.input_device_codec.InputDeviceCodec"]
    """The codec for the video that the device produces."""
    mediaconnect_settings: NotRequired[
        "capo_medialive.types.input_device_media_connect_settings.InputDeviceMediaConnectSettings"
    ]
    """Information about the MediaConnect flow attached to the device. Returned only if the outputType is MEDIACONNECT_FLOW."""
    audio_channel_pairs: NotRequired[
        "capo_medialive.types.__list_of_input_device_uhd_audio_channel_pair_config.__listOfInputDeviceUhdAudioChannelPairConfig"
    ]
    """An array of eight audio configurations, one for each audio pair in the source. Each audio configuration specifies either to exclude the pair, or to format it and include it in the output from the UHD device. Applies only when the device is configured as the source for a MediaConnect flow."""
    input_resolution: NotRequired["capo_medialive.types.__string.__string"]
    """The resolution of the Link device's source (HD or UHD). This value determines MediaLive resource allocation and billing for this input."""


# --- restJson1 ser/de ---
def serialize_json(value: InputDeviceUhdSettings) -> dict:
    out: dict = {}
    if "active_input" in value:
        import capo_medialive.types.input_device_active_input

        out["activeInput"] = (
            capo_medialive.types.input_device_active_input.serialize_json(
                value["active_input"]
            )
        )
    if "configured_input" in value:
        import capo_medialive.types.input_device_configured_input

        out["configuredInput"] = (
            capo_medialive.types.input_device_configured_input.serialize_json(
                value["configured_input"]
            )
        )
    if "device_state" in value:
        import capo_medialive.types.input_device_state

        out["deviceState"] = capo_medialive.types.input_device_state.serialize_json(
            value["device_state"]
        )
    if "framerate" in value:
        out["framerate"] = value["framerate"]
    if "height" in value:
        out["height"] = value["height"]
    if "max_bitrate" in value:
        out["maxBitrate"] = value["max_bitrate"]
    if "scan_type" in value:
        import capo_medialive.types.input_device_scan_type

        out["scanType"] = capo_medialive.types.input_device_scan_type.serialize_json(
            value["scan_type"]
        )
    if "width" in value:
        out["width"] = value["width"]
    if "latency_ms" in value:
        out["latencyMs"] = value["latency_ms"]
    if "codec" in value:
        import capo_medialive.types.input_device_codec

        out["codec"] = capo_medialive.types.input_device_codec.serialize_json(
            value["codec"]
        )
    if "mediaconnect_settings" in value:
        import capo_medialive.types.input_device_media_connect_settings

        out["mediaconnectSettings"] = (
            capo_medialive.types.input_device_media_connect_settings.serialize_json(
                value["mediaconnect_settings"]
            )
        )
    if "audio_channel_pairs" in value:
        import capo_medialive.types.__list_of_input_device_uhd_audio_channel_pair_config

        out["audioChannelPairs"] = (
            capo_medialive.types.__list_of_input_device_uhd_audio_channel_pair_config.serialize_json(
                value["audio_channel_pairs"]
            )
        )
    if "input_resolution" in value:
        out["inputResolution"] = value["input_resolution"]
    return out


def deserialize_json(data: dict) -> InputDeviceUhdSettings:
    out: InputDeviceUhdSettings = {}  # type: ignore[typeddict-item]
    if "activeInput" in data:
        import capo_medialive.types.input_device_active_input

        out["active_input"] = (
            capo_medialive.types.input_device_active_input.deserialize_json(
                data["activeInput"]
            )
        )
    if "configuredInput" in data:
        import capo_medialive.types.input_device_configured_input

        out["configured_input"] = (
            capo_medialive.types.input_device_configured_input.deserialize_json(
                data["configuredInput"]
            )
        )
    if "deviceState" in data:
        import capo_medialive.types.input_device_state

        out["device_state"] = capo_medialive.types.input_device_state.deserialize_json(
            data["deviceState"]
        )
    if "framerate" in data:
        out["framerate"] = data["framerate"]
    if "height" in data:
        out["height"] = data["height"]
    if "maxBitrate" in data:
        out["max_bitrate"] = data["maxBitrate"]
    if "scanType" in data:
        import capo_medialive.types.input_device_scan_type

        out["scan_type"] = capo_medialive.types.input_device_scan_type.deserialize_json(
            data["scanType"]
        )
    if "width" in data:
        out["width"] = data["width"]
    if "latencyMs" in data:
        out["latency_ms"] = data["latencyMs"]
    if "codec" in data:
        import capo_medialive.types.input_device_codec

        out["codec"] = capo_medialive.types.input_device_codec.deserialize_json(
            data["codec"]
        )
    if "mediaconnectSettings" in data:
        import capo_medialive.types.input_device_media_connect_settings

        out["mediaconnect_settings"] = (
            capo_medialive.types.input_device_media_connect_settings.deserialize_json(
                data["mediaconnectSettings"]
            )
        )
    if "audioChannelPairs" in data:
        import capo_medialive.types.__list_of_input_device_uhd_audio_channel_pair_config

        out["audio_channel_pairs"] = (
            capo_medialive.types.__list_of_input_device_uhd_audio_channel_pair_config.deserialize_json(
                data["audioChannelPairs"]
            )
        )
    if "inputResolution" in data:
        out["input_resolution"] = data["inputResolution"]
    return out
