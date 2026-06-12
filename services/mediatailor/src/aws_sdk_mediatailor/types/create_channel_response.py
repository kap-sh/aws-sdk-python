"""Generated from Smithy shape ``com.amazonaws.mediatailor#CreateChannelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__map_of__string
    import aws_sdk_mediatailor.types.__string
    import aws_sdk_mediatailor.types.__timestamp_unix
    import aws_sdk_mediatailor.types.audiences
    import aws_sdk_mediatailor.types.channel_state
    import aws_sdk_mediatailor.types.response_outputs
    import aws_sdk_mediatailor.types.slate_source
    import aws_sdk_mediatailor.types.time_shift_configuration


class CreateChannelResponse(TypedDict):
    arn: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) to assign to the channel.</p>"""
    channel_name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The name to assign to the channel.</p>"""
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
    """<p>The output properties to assign to the channel.</p>"""
    playback_mode: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The playback mode to assign to the channel.</p>"""
    tags: NotRequired["aws_sdk_mediatailor.types.__map_of__string.__mapOf__string"]
    """<p>The tags to assign to the channel. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""
    tier: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The tier of the channel.</p>"""
    time_shift_configuration: NotRequired[
        "aws_sdk_mediatailor.types.time_shift_configuration.TimeShiftConfiguration"
    ]
    """<p> The time-shifted viewing configuration assigned to the channel. </p>"""
    audiences: NotRequired["aws_sdk_mediatailor.types.audiences.Audiences"]
    """<p>The list of audiences defined in channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelResponse) -> dict:
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


def deserialize_json(data: dict) -> CreateChannelResponse:
    out: CreateChannelResponse = {}  # type: ignore[typeddict-item]
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
