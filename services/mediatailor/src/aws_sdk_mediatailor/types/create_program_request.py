"""Generated from Smithy shape ``com.amazonaws.mediatailor#CreateProgramRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__list_of_ad_break
    import aws_sdk_mediatailor.types.__list_of_audience_media
    import aws_sdk_mediatailor.types.__map_of__string
    import aws_sdk_mediatailor.types.__string
    import aws_sdk_mediatailor.types.schedule_configuration


class CreateProgramRequest(TypedDict, closed=True):
    ad_breaks: NotRequired[
        "aws_sdk_mediatailor.types.__list_of_ad_break.__listOfAdBreak"
    ]
    """<p>The ad break configuration settings.</p>"""
    channel_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the channel for this Program.</p>"""
    live_source_name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The name of the LiveSource for this Program.</p>"""
    program_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the Program.</p>"""
    schedule_configuration: (
        "aws_sdk_mediatailor.types.schedule_configuration.ScheduleConfiguration"
    )
    """<p>The schedule configuration settings.</p>"""
    source_location_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the source location.</p>"""
    vod_source_name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The name that's used to refer to a VOD source.</p>"""
    audience_media: NotRequired[
        "aws_sdk_mediatailor.types.__list_of_audience_media.__listOfAudienceMedia"
    ]
    """<p>The list of AudienceMedia defined in program.</p>"""
    tags: NotRequired["aws_sdk_mediatailor.types.__map_of__string.__mapOf__string"]
    r"""<p>The tags to assign to the program. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProgramRequest) -> dict:
    out: dict = {}
    if "ad_breaks" in value:
        import aws_sdk_mediatailor.types.__list_of_ad_break

        out["AdBreaks"] = aws_sdk_mediatailor.types.__list_of_ad_break.serialize_json(
            value["ad_breaks"]
        )
    if "live_source_name" in value:
        out["LiveSourceName"] = value["live_source_name"]
    import aws_sdk_mediatailor.types.schedule_configuration

    out["ScheduleConfiguration"] = (
        aws_sdk_mediatailor.types.schedule_configuration.serialize_json(
            value["schedule_configuration"]
        )
    )
    out["SourceLocationName"] = value["source_location_name"]
    if "vod_source_name" in value:
        out["VodSourceName"] = value["vod_source_name"]
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


def deserialize_json(data: dict) -> CreateProgramRequest:
    out: CreateProgramRequest = {}  # type: ignore[typeddict-item]
    if "AdBreaks" in data:
        import aws_sdk_mediatailor.types.__list_of_ad_break

        out["ad_breaks"] = (
            aws_sdk_mediatailor.types.__list_of_ad_break.deserialize_json(
                data["AdBreaks"]
            )
        )
    if "LiveSourceName" in data:
        out["live_source_name"] = data["LiveSourceName"]
    if "ScheduleConfiguration" in data:
        import aws_sdk_mediatailor.types.schedule_configuration

        out["schedule_configuration"] = (
            aws_sdk_mediatailor.types.schedule_configuration.deserialize_json(
                data["ScheduleConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateProgramRequest.schedule_configuration required"
        )
    if "SourceLocationName" in data:
        out["source_location_name"] = data["SourceLocationName"]
    else:
        raise DeserializationError("CreateProgramRequest.source_location_name required")
    if "VodSourceName" in data:
        out["vod_source_name"] = data["VodSourceName"]
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
