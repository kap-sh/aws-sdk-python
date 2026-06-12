"""Generated from Smithy shape ``com.amazonaws.mediatailor#UpdateProgramResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__list_of_ad_break
    import aws_sdk_mediatailor.types.__list_of_audience_media
    import aws_sdk_mediatailor.types.__long
    import aws_sdk_mediatailor.types.__map_of__string
    import aws_sdk_mediatailor.types.__string
    import aws_sdk_mediatailor.types.__timestamp_unix
    import aws_sdk_mediatailor.types.clip_range


class UpdateProgramResponse(TypedDict):
    ad_breaks: NotRequired[
        "aws_sdk_mediatailor.types.__list_of_ad_break.__listOfAdBreak"
    ]
    """<p>The ad break configuration settings.</p>"""
    arn: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The ARN to assign to the program.</p>"""
    channel_name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The name to assign to the channel for this program.</p>"""
    creation_time: NotRequired[
        "aws_sdk_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The time the program was created.</p>"""
    program_name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The name to assign to this program.</p>"""
    source_location_name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The name to assign to the source location for this program.</p>"""
    vod_source_name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The name that's used to refer to a VOD source.</p>"""
    live_source_name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The name of the LiveSource for this Program.</p>"""
    clip_range: NotRequired["aws_sdk_mediatailor.types.clip_range.ClipRange"]
    """<p>The clip range configuration settings.</p>"""
    duration_millis: NotRequired["aws_sdk_mediatailor.types.__long.__long"]
    """<p>The duration of the live program in milliseconds.</p>"""
    scheduled_start_time: NotRequired[
        "aws_sdk_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The scheduled start time for this Program.</p>"""
    audience_media: NotRequired[
        "aws_sdk_mediatailor.types.__list_of_audience_media.__listOfAudienceMedia"
    ]
    """<p>The list of AudienceMedia defined in program.</p>"""
    tags: NotRequired["aws_sdk_mediatailor.types.__map_of__string.__mapOf__string"]
    """<p>The tags assigned to the program. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProgramResponse) -> dict:
    out: dict = {}
    if "ad_breaks" in value:
        import aws_sdk_mediatailor.types.__list_of_ad_break

        out["AdBreaks"] = aws_sdk_mediatailor.types.__list_of_ad_break.serialize_json(
            value["ad_breaks"]
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "channel_name" in value:
        out["ChannelName"] = value["channel_name"]
    if "creation_time" in value:
        import aws_sdk_mediatailor.types.__timestamp_unix

        out["CreationTime"] = aws_sdk_mediatailor.types.__timestamp_unix.serialize_json(
            value["creation_time"]
        )
    if "program_name" in value:
        out["ProgramName"] = value["program_name"]
    if "source_location_name" in value:
        out["SourceLocationName"] = value["source_location_name"]
    if "vod_source_name" in value:
        out["VodSourceName"] = value["vod_source_name"]
    if "live_source_name" in value:
        out["LiveSourceName"] = value["live_source_name"]
    if "clip_range" in value:
        import aws_sdk_mediatailor.types.clip_range

        out["ClipRange"] = aws_sdk_mediatailor.types.clip_range.serialize_json(
            value["clip_range"]
        )
    if "duration_millis" in value:
        out["DurationMillis"] = value["duration_millis"]
    if "scheduled_start_time" in value:
        import aws_sdk_mediatailor.types.__timestamp_unix

        out["ScheduledStartTime"] = (
            aws_sdk_mediatailor.types.__timestamp_unix.serialize_json(
                value["scheduled_start_time"]
            )
        )
    if "audience_media" in value:
        import aws_sdk_mediatailor.types.__list_of_audience_media

        out["AudienceMedia"] = (
            aws_sdk_mediatailor.types.__list_of_audience_media.serialize_json(
                value["audience_media"]
            )
        )
    if "tags" in value:
        import aws_sdk_mediatailor.types.__map_of__string

        out["tags"] = aws_sdk_mediatailor.types.__map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> UpdateProgramResponse:
    out: UpdateProgramResponse = {}  # type: ignore[typeddict-item]
    if "AdBreaks" in data:
        import aws_sdk_mediatailor.types.__list_of_ad_break

        out["ad_breaks"] = (
            aws_sdk_mediatailor.types.__list_of_ad_break.deserialize_json(
                data["AdBreaks"]
            )
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "ChannelName" in data:
        out["channel_name"] = data["ChannelName"]
    if "CreationTime" in data:
        import aws_sdk_mediatailor.types.__timestamp_unix

        out["creation_time"] = (
            aws_sdk_mediatailor.types.__timestamp_unix.deserialize_json(
                data["CreationTime"]
            )
        )
    if "ProgramName" in data:
        out["program_name"] = data["ProgramName"]
    if "SourceLocationName" in data:
        out["source_location_name"] = data["SourceLocationName"]
    if "VodSourceName" in data:
        out["vod_source_name"] = data["VodSourceName"]
    if "LiveSourceName" in data:
        out["live_source_name"] = data["LiveSourceName"]
    if "ClipRange" in data:
        import aws_sdk_mediatailor.types.clip_range

        out["clip_range"] = aws_sdk_mediatailor.types.clip_range.deserialize_json(
            data["ClipRange"]
        )
    if "DurationMillis" in data:
        out["duration_millis"] = data["DurationMillis"]
    if "ScheduledStartTime" in data:
        import aws_sdk_mediatailor.types.__timestamp_unix

        out["scheduled_start_time"] = (
            aws_sdk_mediatailor.types.__timestamp_unix.deserialize_json(
                data["ScheduledStartTime"]
            )
        )
    if "AudienceMedia" in data:
        import aws_sdk_mediatailor.types.__list_of_audience_media

        out["audience_media"] = (
            aws_sdk_mediatailor.types.__list_of_audience_media.deserialize_json(
                data["AudienceMedia"]
            )
        )
    if "tags" in data:
        import aws_sdk_mediatailor.types.__map_of__string

        out["tags"] = aws_sdk_mediatailor.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    return out
