"""Generated from Smithy shape ``com.amazonaws.ivs#ChannelSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ivs.types.channel_ad_configuration_arn
    import aws_sdk_ivs.types.channel_arn
    import aws_sdk_ivs.types.channel_latency_mode
    import aws_sdk_ivs.types.channel_name
    import aws_sdk_ivs.types.channel_playback_restriction_policy_arn
    import aws_sdk_ivs.types.channel_recording_configuration_arn
    import aws_sdk_ivs.types.channel_type
    import aws_sdk_ivs.types.insecure_ingest
    import aws_sdk_ivs.types.is_authorized
    import aws_sdk_ivs.types.tags
    import aws_sdk_ivs.types.transcode_preset


class ChannelSummary(TypedDict):
    arn: NotRequired["aws_sdk_ivs.types.channel_arn.ChannelArn"]
    """<p>Channel ARN.</p>"""
    name: NotRequired["aws_sdk_ivs.types.channel_name.ChannelName"]
    """<p>Channel name.</p>"""
    latency_mode: NotRequired[
        "aws_sdk_ivs.types.channel_latency_mode.ChannelLatencyMode"
    ]
    """<p>Channel latency mode. Use <code>NORMAL</code> to broadcast and deliver live video up to Full HD. Use <code>LOW</code> for near-real-time interaction with viewers. Default: <code>LOW</code>.</p>"""
    authorized: "aws_sdk_ivs.types.is_authorized.IsAuthorized"
    """<p>Whether the channel is private (enabled for playback authorization). Default: <code>false</code>.</p>"""
    recording_configuration_arn: NotRequired[
        "aws_sdk_ivs.types.channel_recording_configuration_arn.ChannelRecordingConfigurationArn"
    ]
    r"""<p>Recording-configuration ARN. A valid ARN value here both specifies the ARN and enables recording. Default: \"\" (empty string, recording is disabled).</p>"""
    tags: NotRequired["aws_sdk_ivs.types.tags.Tags"]
    r"""<p>Tags attached to the resource. Array of 1-50 maps, each of the form <code>string:string (key:value)</code>. See <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html\">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>"""
    insecure_ingest: "aws_sdk_ivs.types.insecure_ingest.InsecureIngest"
    """<p>Whether the channel allows insecure RTMP ingest. Default: <code>false</code>.</p>"""
    type: NotRequired["aws_sdk_ivs.types.channel_type.ChannelType"]
    r"""<p>Channel type, which determines the allowable resolution and bitrate. <i>If you exceed the allowable input resolution or bitrate, the stream probably will disconnect immediately.</i> Default: <code>STANDARD</code>. For details, see <a href=\"https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/channel-types.html\">Channel Types</a>.</p>"""
    preset: NotRequired["aws_sdk_ivs.types.transcode_preset.TranscodePreset"]
    r"""<p>Optional transcode preset for the channel. This is selectable only for <code>ADVANCED_HD</code> and <code>ADVANCED_SD</code> channel types. For those channel types, the default <code>preset</code> is <code>HIGHER_BANDWIDTH_DELIVERY</code>. For other channel types (<code>BASIC</code> and <code>STANDARD</code>), <code>preset</code> is the empty string (<code>\"\"</code>).</p>"""
    playback_restriction_policy_arn: NotRequired[
        "aws_sdk_ivs.types.channel_playback_restriction_policy_arn.ChannelPlaybackRestrictionPolicyArn"
    ]
    r"""<p>Playback-restriction-policy ARN. A valid ARN value here both specifies the ARN and enables playback restriction. Default: \"\" (empty string, no playback restriction policy is applied).</p>"""
    ad_configuration_arn: NotRequired[
        "aws_sdk_ivs.types.channel_ad_configuration_arn.ChannelAdConfigurationArn"
    ]
    """<p>ARN of the ad configuration associated with the channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "latency_mode" in value:
        out["latencyMode"] = value["latency_mode"]
    out["authorized"] = value.get("authorized", False)
    if "recording_configuration_arn" in value:
        out["recordingConfigurationArn"] = value["recording_configuration_arn"]
    if "tags" in value:
        import aws_sdk_ivs.types.tags

        out["tags"] = aws_sdk_ivs.types.tags.serialize_json(value["tags"])
    out["insecureIngest"] = value.get("insecure_ingest", False)
    if "type" in value:
        import aws_sdk_ivs.types.channel_type

        out["type"] = aws_sdk_ivs.types.channel_type.serialize_json(value["type"])
    if "preset" in value:
        import aws_sdk_ivs.types.transcode_preset

        out["preset"] = aws_sdk_ivs.types.transcode_preset.serialize_json(
            value["preset"]
        )
    if "playback_restriction_policy_arn" in value:
        out["playbackRestrictionPolicyArn"] = value["playback_restriction_policy_arn"]
    if "ad_configuration_arn" in value:
        out["adConfigurationArn"] = value["ad_configuration_arn"]
    return out


def deserialize_json(data: dict) -> ChannelSummary:
    out: ChannelSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "latencyMode" in data:
        out["latency_mode"] = data["latencyMode"]
    if "authorized" in data:
        out["authorized"] = data["authorized"]
    else:
        out["authorized"] = False
    if "recordingConfigurationArn" in data:
        out["recording_configuration_arn"] = data["recordingConfigurationArn"]
    if "tags" in data:
        import aws_sdk_ivs.types.tags

        out["tags"] = aws_sdk_ivs.types.tags.deserialize_json(data["tags"])
    if "insecureIngest" in data:
        out["insecure_ingest"] = data["insecureIngest"]
    else:
        out["insecure_ingest"] = False
    if "type" in data:
        import aws_sdk_ivs.types.channel_type

        out["type"] = aws_sdk_ivs.types.channel_type.deserialize_json(data["type"])
    if "preset" in data:
        import aws_sdk_ivs.types.transcode_preset

        out["preset"] = aws_sdk_ivs.types.transcode_preset.deserialize_json(
            data["preset"]
        )
    if "playbackRestrictionPolicyArn" in data:
        out["playback_restriction_policy_arn"] = data["playbackRestrictionPolicyArn"]
    if "adConfigurationArn" in data:
        out["ad_configuration_arn"] = data["adConfigurationArn"]
    return out
