"""Generated from Smithy shape ``com.amazonaws.ivs#UpdateChannelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.boolean
    import aws_sdk_ivs.types.channel_ad_configuration_arn
    import aws_sdk_ivs.types.channel_arn
    import aws_sdk_ivs.types.channel_latency_mode
    import aws_sdk_ivs.types.channel_name
    import aws_sdk_ivs.types.channel_playback_restriction_policy_arn
    import aws_sdk_ivs.types.channel_recording_configuration_arn
    import aws_sdk_ivs.types.channel_type
    import aws_sdk_ivs.types.container_format
    import aws_sdk_ivs.types.multitrack_input_configuration
    import aws_sdk_ivs.types.transcode_preset


class UpdateChannelRequest(TypedDict):
    arn: "aws_sdk_ivs.types.channel_arn.ChannelArn"
    """<p>ARN of the channel to be updated.</p>"""
    name: NotRequired["aws_sdk_ivs.types.channel_name.ChannelName"]
    """<p>Channel name.</p>"""
    latency_mode: NotRequired[
        "aws_sdk_ivs.types.channel_latency_mode.ChannelLatencyMode"
    ]
    """<p>Channel latency mode. Use <code>NORMAL</code> to broadcast and deliver live video up to Full HD. Use <code>LOW</code> for near-real-time interaction with viewers.</p>"""
    type: NotRequired["aws_sdk_ivs.types.channel_type.ChannelType"]
    """<p>Channel type, which determines the allowable resolution and bitrate. <i>If you exceed the allowable input resolution or bitrate, the stream probably will disconnect immediately.</i> Default: <code>STANDARD</code>. For details, see <a href=\"https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/channel-types.html\">Channel Types</a>.</p>"""
    authorized: "aws_sdk_ivs.types.boolean.Boolean"
    """<p>Whether the channel is private (enabled for playback authorization).</p>"""
    recording_configuration_arn: NotRequired[
        "aws_sdk_ivs.types.channel_recording_configuration_arn.ChannelRecordingConfigurationArn"
    ]
    """<p>Recording-configuration ARN. A valid ARN value here both specifies the ARN and enables recording. If this is set to an empty string, recording is disabled.</p>"""
    insecure_ingest: "aws_sdk_ivs.types.boolean.Boolean"
    """<p>Whether the channel allows insecure RTMP and SRT ingest. Default: <code>false</code>.</p>"""
    preset: NotRequired["aws_sdk_ivs.types.transcode_preset.TranscodePreset"]
    """<p>Optional transcode preset for the channel. This is selectable only for <code>ADVANCED_HD</code> and <code>ADVANCED_SD</code> channel types. For those channel types, the default <code>preset</code> is <code>HIGHER_BANDWIDTH_DELIVERY</code>. For other channel types (<code>BASIC</code> and <code>STANDARD</code>), <code>preset</code> is the empty string (<code>\"\"</code>).</p>"""
    playback_restriction_policy_arn: NotRequired[
        "aws_sdk_ivs.types.channel_playback_restriction_policy_arn.ChannelPlaybackRestrictionPolicyArn"
    ]
    """<p>Playback-restriction-policy ARN. A valid ARN value here both specifies the ARN and enables playback restriction. If this is set to an empty string, playback restriction policy is disabled.</p>"""
    multitrack_input_configuration: NotRequired[
        "aws_sdk_ivs.types.multitrack_input_configuration.MultitrackInputConfiguration"
    ]
    """<p>Object specifying multitrack input configuration. Default: no multitrack input configuration is specified.</p>"""
    container_format: NotRequired["aws_sdk_ivs.types.container_format.ContainerFormat"]
    """<p>Indicates which content-packaging format is used (MPEG-TS or fMP4). If <code>multitrackInputConfiguration</code> is specified and <code>enabled</code> is <code>true</code>, then <code>containerFormat</code> is required and must be set to <code>FRAGMENTED_MP4</code>. Otherwise, <code>containerFormat</code> may be set to <code>TS</code> or <code>FRAGMENTED_MP4</code>. Default: <code>TS</code>.</p>"""
    ad_configuration_arn: NotRequired[
        "aws_sdk_ivs.types.channel_ad_configuration_arn.ChannelAdConfigurationArn"
    ]
    """<p>ARN of the ad configuration associated with the channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "latency_mode" in value:
        out["latencyMode"] = value["latency_mode"]
    if "type" in value:
        import aws_sdk_ivs.types.channel_type

        out["type"] = aws_sdk_ivs.types.channel_type.serialize_json(value["type"])
    out["authorized"] = value.get("authorized", False)
    if "recording_configuration_arn" in value:
        out["recordingConfigurationArn"] = value["recording_configuration_arn"]
    out["insecureIngest"] = value.get("insecure_ingest", False)
    if "preset" in value:
        import aws_sdk_ivs.types.transcode_preset

        out["preset"] = aws_sdk_ivs.types.transcode_preset.serialize_json(
            value["preset"]
        )
    if "playback_restriction_policy_arn" in value:
        out["playbackRestrictionPolicyArn"] = value["playback_restriction_policy_arn"]
    if "multitrack_input_configuration" in value:
        import aws_sdk_ivs.types.multitrack_input_configuration

        out["multitrackInputConfiguration"] = (
            aws_sdk_ivs.types.multitrack_input_configuration.serialize_json(
                value["multitrack_input_configuration"]
            )
        )
    if "container_format" in value:
        out["containerFormat"] = value["container_format"]
    if "ad_configuration_arn" in value:
        out["adConfigurationArn"] = value["ad_configuration_arn"]
    return out


def deserialize_json(data: dict) -> UpdateChannelRequest:
    out: UpdateChannelRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdateChannelRequest.arn required")
    if "name" in data:
        out["name"] = data["name"]
    if "latencyMode" in data:
        out["latency_mode"] = data["latencyMode"]
    if "type" in data:
        import aws_sdk_ivs.types.channel_type

        out["type"] = aws_sdk_ivs.types.channel_type.deserialize_json(data["type"])
    if "authorized" in data:
        out["authorized"] = data["authorized"]
    else:
        out["authorized"] = False
    if "recordingConfigurationArn" in data:
        out["recording_configuration_arn"] = data["recordingConfigurationArn"]
    if "insecureIngest" in data:
        out["insecure_ingest"] = data["insecureIngest"]
    else:
        out["insecure_ingest"] = False
    if "preset" in data:
        import aws_sdk_ivs.types.transcode_preset

        out["preset"] = aws_sdk_ivs.types.transcode_preset.deserialize_json(
            data["preset"]
        )
    if "playbackRestrictionPolicyArn" in data:
        out["playback_restriction_policy_arn"] = data["playbackRestrictionPolicyArn"]
    if "multitrackInputConfiguration" in data:
        import aws_sdk_ivs.types.multitrack_input_configuration

        out["multitrack_input_configuration"] = (
            aws_sdk_ivs.types.multitrack_input_configuration.deserialize_json(
                data["multitrackInputConfiguration"]
            )
        )
    if "containerFormat" in data:
        out["container_format"] = data["containerFormat"]
    if "adConfigurationArn" in data:
        out["ad_configuration_arn"] = data["adConfigurationArn"]
    return out
