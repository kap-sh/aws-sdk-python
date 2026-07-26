"""Generated from Smithy shape ``com.amazonaws.mediatailor#ScheduleAdBreak``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__long
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.__timestamp_unix


class ScheduleAdBreak(TypedDict, closed=True):
    approximate_duration_seconds: NotRequired["capo_mediatailor.types.__long.__long"]
    """<p>The approximate duration of the ad break, in seconds.</p>"""
    approximate_start_time: NotRequired[
        "capo_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The approximate time that the ad will start playing.</p>"""
    source_location_name: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The name of the source location containing the VOD source used for the ad break.</p>"""
    vod_source_name: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The name of the VOD source used for the ad break.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleAdBreak) -> dict:
    out: dict = {}
    if "approximate_duration_seconds" in value:
        out["ApproximateDurationSeconds"] = value["approximate_duration_seconds"]
    if "approximate_start_time" in value:
        import capo_mediatailor.types.__timestamp_unix

        out["ApproximateStartTime"] = (
            capo_mediatailor.types.__timestamp_unix.serialize_json(
                value["approximate_start_time"]
            )
        )
    if "source_location_name" in value:
        out["SourceLocationName"] = value["source_location_name"]
    if "vod_source_name" in value:
        out["VodSourceName"] = value["vod_source_name"]
    return out


def deserialize_json(data: dict) -> ScheduleAdBreak:
    out: ScheduleAdBreak = {}  # type: ignore[typeddict-item]
    if "ApproximateDurationSeconds" in data:
        out["approximate_duration_seconds"] = data["ApproximateDurationSeconds"]
    if "ApproximateStartTime" in data:
        import capo_mediatailor.types.__timestamp_unix

        out["approximate_start_time"] = (
            capo_mediatailor.types.__timestamp_unix.deserialize_json(
                data["ApproximateStartTime"]
            )
        )
    if "SourceLocationName" in data:
        out["source_location_name"] = data["SourceLocationName"]
    if "VodSourceName" in data:
        out["vod_source_name"] = data["VodSourceName"]
    return out
