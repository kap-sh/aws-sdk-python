"""Generated from Smithy shape ``com.amazonaws.mediatailor#ScheduleEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__list_of_schedule_ad_break
    import aws_sdk_mediatailor.types.__long
    import aws_sdk_mediatailor.types.__string
    import aws_sdk_mediatailor.types.__timestamp_unix
    import aws_sdk_mediatailor.types.audiences
    import aws_sdk_mediatailor.types.schedule_entry_type


class ScheduleEntry(TypedDict, closed=True):
    approximate_duration_seconds: NotRequired["aws_sdk_mediatailor.types.__long.__long"]
    """<p>The approximate duration of this program, in seconds.</p>"""
    approximate_start_time: NotRequired[
        "aws_sdk_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The approximate time that the program will start playing.</p>"""
    arn: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The ARN of the program.</p>"""
    channel_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the channel that uses this schedule.</p>"""
    live_source_name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The name of the live source used for the program.</p>"""
    program_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the program.</p>"""
    schedule_ad_breaks: NotRequired[
        "aws_sdk_mediatailor.types.__list_of_schedule_ad_break.__listOfScheduleAdBreak"
    ]
    """<p>The schedule's ad break properties.</p>"""
    schedule_entry_type: NotRequired[
        "aws_sdk_mediatailor.types.schedule_entry_type.ScheduleEntryType"
    ]
    """<p>The type of schedule entry.</p>"""
    source_location_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the source location.</p>"""
    vod_source_name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The name of the VOD source.</p>"""
    audiences: NotRequired["aws_sdk_mediatailor.types.audiences.Audiences"]
    """<p>The list of audiences defined in ScheduleEntry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleEntry) -> dict:
    out: dict = {}
    if "approximate_duration_seconds" in value:
        out["ApproximateDurationSeconds"] = value["approximate_duration_seconds"]
    if "approximate_start_time" in value:
        import aws_sdk_mediatailor.types.__timestamp_unix

        out["ApproximateStartTime"] = (
            aws_sdk_mediatailor.types.__timestamp_unix.serialize_json(
                value["approximate_start_time"]
            )
        )
    out["Arn"] = value["arn"]
    out["ChannelName"] = value["channel_name"]
    if "live_source_name" in value:
        out["LiveSourceName"] = value["live_source_name"]
    out["ProgramName"] = value["program_name"]
    if "schedule_ad_breaks" in value:
        import aws_sdk_mediatailor.types.__list_of_schedule_ad_break

        out["ScheduleAdBreaks"] = (
            aws_sdk_mediatailor.types.__list_of_schedule_ad_break.serialize_json(
                value["schedule_ad_breaks"]
            )
        )
    if "schedule_entry_type" in value:
        import aws_sdk_mediatailor.types.schedule_entry_type

        out["ScheduleEntryType"] = (
            aws_sdk_mediatailor.types.schedule_entry_type.serialize_json(
                value["schedule_entry_type"]
            )
        )
    out["SourceLocationName"] = value["source_location_name"]
    if "vod_source_name" in value:
        out["VodSourceName"] = value["vod_source_name"]
    if "audiences" in value:
        import aws_sdk_mediatailor.types.audiences

        out["Audiences"] = aws_sdk_mediatailor.types.audiences.serialize_json(
            value["audiences"]
        )
    return out


def deserialize_json(data: dict) -> ScheduleEntry:
    out: ScheduleEntry = {}  # type: ignore[typeddict-item]
    if "ApproximateDurationSeconds" in data:
        out["approximate_duration_seconds"] = data["ApproximateDurationSeconds"]
    if "ApproximateStartTime" in data:
        import aws_sdk_mediatailor.types.__timestamp_unix

        out["approximate_start_time"] = (
            aws_sdk_mediatailor.types.__timestamp_unix.deserialize_json(
                data["ApproximateStartTime"]
            )
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("ScheduleEntry.arn required")
    if "ChannelName" in data:
        out["channel_name"] = data["ChannelName"]
    else:
        raise DeserializationError("ScheduleEntry.channel_name required")
    if "LiveSourceName" in data:
        out["live_source_name"] = data["LiveSourceName"]
    if "ProgramName" in data:
        out["program_name"] = data["ProgramName"]
    else:
        raise DeserializationError("ScheduleEntry.program_name required")
    if "ScheduleAdBreaks" in data:
        import aws_sdk_mediatailor.types.__list_of_schedule_ad_break

        out["schedule_ad_breaks"] = (
            aws_sdk_mediatailor.types.__list_of_schedule_ad_break.deserialize_json(
                data["ScheduleAdBreaks"]
            )
        )
    if "ScheduleEntryType" in data:
        import aws_sdk_mediatailor.types.schedule_entry_type

        out["schedule_entry_type"] = (
            aws_sdk_mediatailor.types.schedule_entry_type.deserialize_json(
                data["ScheduleEntryType"]
            )
        )
    if "SourceLocationName" in data:
        out["source_location_name"] = data["SourceLocationName"]
    else:
        raise DeserializationError("ScheduleEntry.source_location_name required")
    if "VodSourceName" in data:
        out["vod_source_name"] = data["VodSourceName"]
    if "Audiences" in data:
        import aws_sdk_mediatailor.types.audiences

        out["audiences"] = aws_sdk_mediatailor.types.audiences.deserialize_json(
            data["Audiences"]
        )
    return out
