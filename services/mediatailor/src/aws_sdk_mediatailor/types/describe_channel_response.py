"""Generated from Smithy shape ``com.amazonaws.mediatailor#DescribeChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__map_of__string
    import aws_sdk_mediatailor.types.__string
    import aws_sdk_mediatailor.types.__timestamp_unix
    import aws_sdk_mediatailor.types.audiences
    import aws_sdk_mediatailor.types.channel_state
    import aws_sdk_mediatailor.types.log_configuration_for_channel
    import aws_sdk_mediatailor.types.response_outputs
    import aws_sdk_mediatailor.types.slate_source
    import aws_sdk_mediatailor.types.time_shift_configuration


class DescribeChannelResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The ARN of the channel.</p>"""
    channel_name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The name of the channel.</p>"""
    channel_state: NotRequired["aws_sdk_mediatailor.types.channel_state.ChannelState"]
    """<p>Indicates whether the channel is in a running state or not.</p>"""
    creation_time: NotRequired[
        "aws_sdk_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The timestamp of when the channel was created.</p>"""
    filler_slate: NotRequired["aws_sdk_mediatailor.types.slate_source.SlateSource"]
    """<p>Contains information about the slate used to fill gaps between programs in the schedule.</p>"""
    last_modified_time: NotRequired[
        "aws_sdk_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The timestamp of when the channel was last modified.</p>"""
    outputs: NotRequired["aws_sdk_mediatailor.types.response_outputs.ResponseOutputs"]
    """<p>The channel's output properties.</p>"""
    playback_mode: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The channel's playback mode.</p>"""
    tags: NotRequired["aws_sdk_mediatailor.types.__map_of__string.__mapOf__string"]
    r"""<p>The tags assigned to the channel. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""
    tier: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The channel's tier.</p>"""
    log_configuration: "aws_sdk_mediatailor.types.log_configuration_for_channel.LogConfigurationForChannel"
    """<p>The log configuration for the channel.</p>"""
    time_shift_configuration: NotRequired[
        "aws_sdk_mediatailor.types.time_shift_configuration.TimeShiftConfiguration"
    ]
    """<p> The time-shifted viewing configuration for the channel. </p>"""
    audiences: NotRequired["aws_sdk_mediatailor.types.audiences.Audiences"]
    """<p>The list of audiences defined in channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeChannelResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "channel_name" in value:
        out["ChannelName"] = value["channel_name"]
    if "channel_state" in value:
        import aws_sdk_mediatailor.types.channel_state

        out["ChannelState"] = aws_sdk_mediatailor.types.channel_state.serialize_json(
            value["channel_state"]
        )
    if "creation_time" in value:
        import aws_sdk_mediatailor.types.__timestamp_unix

        out["CreationTime"] = aws_sdk_mediatailor.types.__timestamp_unix.serialize_json(
            value["creation_time"]
        )
    if "filler_slate" in value:
        import aws_sdk_mediatailor.types.slate_source

        out["FillerSlate"] = aws_sdk_mediatailor.types.slate_source.serialize_json(
            value["filler_slate"]
        )
    if "last_modified_time" in value:
        import aws_sdk_mediatailor.types.__timestamp_unix

        out["LastModifiedTime"] = (
            aws_sdk_mediatailor.types.__timestamp_unix.serialize_json(
                value["last_modified_time"]
            )
        )
    if "outputs" in value:
        import aws_sdk_mediatailor.types.response_outputs

        out["Outputs"] = aws_sdk_mediatailor.types.response_outputs.serialize_json(
            value["outputs"]
        )
    if "playback_mode" in value:
        out["PlaybackMode"] = value["playback_mode"]
    if "tags" in value:
        import aws_sdk_mediatailor.types.__map_of__string

        out["tags"] = aws_sdk_mediatailor.types.__map_of__string.serialize_json(
            value["tags"]
        )
    if "tier" in value:
        out["Tier"] = value["tier"]
    import aws_sdk_mediatailor.types.log_configuration_for_channel

    out["LogConfiguration"] = (
        aws_sdk_mediatailor.types.log_configuration_for_channel.serialize_json(
            value["log_configuration"]
        )
    )
    if "time_shift_configuration" in value:
        import aws_sdk_mediatailor.types.time_shift_configuration

        out["TimeShiftConfiguration"] = (
            aws_sdk_mediatailor.types.time_shift_configuration.serialize_json(
                value["time_shift_configuration"]
            )
        )
    if "audiences" in value:
        import aws_sdk_mediatailor.types.audiences

        out["Audiences"] = aws_sdk_mediatailor.types.audiences.serialize_json(
            value["audiences"]
        )
    return out


def deserialize_json(data: dict) -> DescribeChannelResponse:
    out: DescribeChannelResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "ChannelName" in data:
        out["channel_name"] = data["ChannelName"]
    if "ChannelState" in data:
        import aws_sdk_mediatailor.types.channel_state

        out["channel_state"] = aws_sdk_mediatailor.types.channel_state.deserialize_json(
            data["ChannelState"]
        )
    if "CreationTime" in data:
        import aws_sdk_mediatailor.types.__timestamp_unix

        out["creation_time"] = (
            aws_sdk_mediatailor.types.__timestamp_unix.deserialize_json(
                data["CreationTime"]
            )
        )
    if "FillerSlate" in data:
        import aws_sdk_mediatailor.types.slate_source

        out["filler_slate"] = aws_sdk_mediatailor.types.slate_source.deserialize_json(
            data["FillerSlate"]
        )
    if "LastModifiedTime" in data:
        import aws_sdk_mediatailor.types.__timestamp_unix

        out["last_modified_time"] = (
            aws_sdk_mediatailor.types.__timestamp_unix.deserialize_json(
                data["LastModifiedTime"]
            )
        )
    if "Outputs" in data:
        import aws_sdk_mediatailor.types.response_outputs

        out["outputs"] = aws_sdk_mediatailor.types.response_outputs.deserialize_json(
            data["Outputs"]
        )
    if "PlaybackMode" in data:
        out["playback_mode"] = data["PlaybackMode"]
    if "tags" in data:
        import aws_sdk_mediatailor.types.__map_of__string

        out["tags"] = aws_sdk_mediatailor.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    if "Tier" in data:
        out["tier"] = data["Tier"]
    if "LogConfiguration" in data:
        import aws_sdk_mediatailor.types.log_configuration_for_channel

        out["log_configuration"] = (
            aws_sdk_mediatailor.types.log_configuration_for_channel.deserialize_json(
                data["LogConfiguration"]
            )
        )
    else:
        raise DeserializationError("DescribeChannelResponse.log_configuration required")
    if "TimeShiftConfiguration" in data:
        import aws_sdk_mediatailor.types.time_shift_configuration

        out["time_shift_configuration"] = (
            aws_sdk_mediatailor.types.time_shift_configuration.deserialize_json(
                data["TimeShiftConfiguration"]
            )
        )
    if "Audiences" in data:
        import aws_sdk_mediatailor.types.audiences

        out["audiences"] = aws_sdk_mediatailor.types.audiences.deserialize_json(
            data["Audiences"]
        )
    return out
