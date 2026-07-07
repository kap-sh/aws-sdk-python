"""Generated from Smithy shape ``com.amazonaws.mediatailor#AlternateMedia``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__list_of_ad_break
    import aws_sdk_mediatailor.types.__long
    import aws_sdk_mediatailor.types.__string
    import aws_sdk_mediatailor.types.clip_range


class AlternateMedia(TypedDict, closed=True):
    source_location_name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The name of the source location for alternateMedia.</p>"""
    live_source_name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The name of the live source for alternateMedia.</p>"""
    vod_source_name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The name of the VOD source for alternateMedia.</p>"""
    clip_range: NotRequired["aws_sdk_mediatailor.types.clip_range.ClipRange"]
    scheduled_start_time_millis: NotRequired["aws_sdk_mediatailor.types.__long.__long"]
    """<p>The date and time that the alternateMedia is scheduled to start, in epoch milliseconds.</p>"""
    ad_breaks: NotRequired[
        "aws_sdk_mediatailor.types.__list_of_ad_break.__listOfAdBreak"
    ]
    """<p>Ad break configuration parameters defined in AlternateMedia.</p>"""
    duration_millis: NotRequired["aws_sdk_mediatailor.types.__long.__long"]
    """<p>The duration of the alternateMedia in milliseconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AlternateMedia) -> dict:
    out: dict = {}
    if "source_location_name" in value:
        out["SourceLocationName"] = value["source_location_name"]
    if "live_source_name" in value:
        out["LiveSourceName"] = value["live_source_name"]
    if "vod_source_name" in value:
        out["VodSourceName"] = value["vod_source_name"]
    if "clip_range" in value:
        import aws_sdk_mediatailor.types.clip_range

        out["ClipRange"] = aws_sdk_mediatailor.types.clip_range.serialize_json(
            value["clip_range"]
        )
    if "scheduled_start_time_millis" in value:
        out["ScheduledStartTimeMillis"] = value["scheduled_start_time_millis"]
    if "ad_breaks" in value:
        import aws_sdk_mediatailor.types.__list_of_ad_break

        out["AdBreaks"] = aws_sdk_mediatailor.types.__list_of_ad_break.serialize_json(
            value["ad_breaks"]
        )
    if "duration_millis" in value:
        out["DurationMillis"] = value["duration_millis"]
    return out


def deserialize_json(data: dict) -> AlternateMedia:
    out: AlternateMedia = {}  # type: ignore[typeddict-item]
    if "SourceLocationName" in data:
        out["source_location_name"] = data["SourceLocationName"]
    if "LiveSourceName" in data:
        out["live_source_name"] = data["LiveSourceName"]
    if "VodSourceName" in data:
        out["vod_source_name"] = data["VodSourceName"]
    if "ClipRange" in data:
        import aws_sdk_mediatailor.types.clip_range

        out["clip_range"] = aws_sdk_mediatailor.types.clip_range.deserialize_json(
            data["ClipRange"]
        )
    if "ScheduledStartTimeMillis" in data:
        out["scheduled_start_time_millis"] = data["ScheduledStartTimeMillis"]
    if "AdBreaks" in data:
        import aws_sdk_mediatailor.types.__list_of_ad_break

        out["ad_breaks"] = (
            aws_sdk_mediatailor.types.__list_of_ad_break.deserialize_json(
                data["AdBreaks"]
            )
        )
    if "DurationMillis" in data:
        out["duration_millis"] = data["DurationMillis"]
    return out
