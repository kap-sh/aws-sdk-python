"""Generated from Smithy shape ``com.amazonaws.mediatailor#DescribeProgramResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__list_of_ad_break
    import aws_sdk_mediatailor.types.__list_of_audience_media
    import aws_sdk_mediatailor.types.__map_of__string
    import aws_sdk_mediatailor.types.__string
    import aws_sdk_mediatailor.types.__timestamp_unix
    import aws_sdk_mediatailor.types.clip_range


class DescribeProgramResponse(TypedDict):
    ad_breaks: NotRequired[
        "aws_sdk_mediatailor.types.__list_of_ad_break.__listOfAdBreak"
    ]
    """<p>The ad break configuration settings.</p>"""
    arn: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The ARN of the program.</p>"""
    channel_name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The name of the channel that the program belongs to.</p>"""
    creation_time: NotRequired[
        "aws_sdk_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The timestamp of when the program was created.</p>"""
    live_source_name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The name of the LiveSource for this Program.</p>"""
    program_name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The name of the program.</p>"""
    scheduled_start_time: NotRequired[
        "aws_sdk_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The date and time that the program is scheduled to start in ISO 8601 format and Coordinated Universal Time (UTC). For example, the value 2021-03-27T17:48:16.751Z represents March 27, 2021 at 17:48:16.751 UTC.</p>"""
    source_location_name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The source location name.</p>"""
    vod_source_name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The name that's used to refer to a VOD source.</p>"""
    clip_range: NotRequired["aws_sdk_mediatailor.types.clip_range.ClipRange"]
    """<p>The clip range configuration settings.</p>"""
    duration_millis: NotRequired["int"]
    """<p>The duration of the live program in milliseconds.</p>"""
    audience_media: NotRequired[
        "aws_sdk_mediatailor.types.__list_of_audience_media.__listOfAudienceMedia"
    ]
    """<p>The list of AudienceMedia defined in program.</p>"""
    tags: NotRequired["aws_sdk_mediatailor.types.__map_of__string.__mapOf__string"]
    r"""<p>The tags assigned to the program. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeProgramResponse) -> dict:
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
    if "live_source_name" in value:
        out["LiveSourceName"] = value["live_source_name"]
    if "program_name" in value:
        out["ProgramName"] = value["program_name"]
    if "scheduled_start_time" in value:
        import aws_sdk_mediatailor.types.__timestamp_unix

        out["ScheduledStartTime"] = (
            aws_sdk_mediatailor.types.__timestamp_unix.serialize_json(
                value["scheduled_start_time"]
            )
        )
    if "source_location_name" in value:
        out["SourceLocationName"] = value["source_location_name"]
    if "vod_source_name" in value:
        out["VodSourceName"] = value["vod_source_name"]
    if "clip_range" in value:
        import aws_sdk_mediatailor.types.clip_range

        out["ClipRange"] = aws_sdk_mediatailor.types.clip_range.serialize_json(
            value["clip_range"]
        )
    if "duration_millis" in value:
        out["DurationMillis"] = value["duration_millis"]
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


def deserialize_json(data: dict) -> DescribeProgramResponse:
    out: DescribeProgramResponse = {}  # type: ignore[typeddict-item]
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
    if "LiveSourceName" in data:
        out["live_source_name"] = data["LiveSourceName"]
    if "ProgramName" in data:
        out["program_name"] = data["ProgramName"]
    if "ScheduledStartTime" in data:
        import aws_sdk_mediatailor.types.__timestamp_unix

        out["scheduled_start_time"] = (
            aws_sdk_mediatailor.types.__timestamp_unix.deserialize_json(
                data["ScheduledStartTime"]
            )
        )
    if "SourceLocationName" in data:
        out["source_location_name"] = data["SourceLocationName"]
    if "VodSourceName" in data:
        out["vod_source_name"] = data["VodSourceName"]
    if "ClipRange" in data:
        import aws_sdk_mediatailor.types.clip_range

        out["clip_range"] = aws_sdk_mediatailor.types.clip_range.deserialize_json(
            data["ClipRange"]
        )
    if "DurationMillis" in data:
        out["duration_millis"] = data["DurationMillis"]
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
