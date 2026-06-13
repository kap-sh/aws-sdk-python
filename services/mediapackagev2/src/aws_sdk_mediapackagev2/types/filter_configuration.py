"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#FilterConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime


class FilterConfiguration(TypedDict):
    manifest_filter: NotRequired["str"]
    """<p>Optionally specify one or more manifest filters for all of your manifest egress requests. When you include a manifest filter, note that you cannot use an identical manifest filter query parameter for this manifest's endpoint URL.</p>"""
    drm_settings: NotRequired["str"]
    """<p>Optionally specify one or more DRM settings for all of your manifest egress requests. When you include a DRM setting, note that you cannot use an identical DRM setting query parameter for this manifest's endpoint URL.</p>"""
    start: NotRequired["datetime.datetime"]
    """<p>Optionally specify the start time for all of your manifest egress requests. When you include start time, note that you cannot use start time query parameters for this manifest's endpoint URL.</p>"""
    end: NotRequired["datetime.datetime"]
    """<p>Optionally specify the end time for all of your manifest egress requests. When you include end time, note that you cannot use end time query parameters for this manifest's endpoint URL.</p>"""
    time_delay_seconds: NotRequired["int"]
    """<p>Optionally specify the time delay for all of your manifest egress requests. Enter a value that is smaller than your endpoint's startover window. When you include time delay, note that you cannot use time delay query parameters for this manifest's endpoint URL.</p>"""
    clip_start_time: NotRequired["datetime.datetime"]
    """<p>Optionally specify the clip start time for all of your manifest egress requests. When you include clip start time, note that you cannot use clip start time query parameters for this manifest's endpoint URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterConfiguration) -> dict:
    out: dict = {}
    if "manifest_filter" in value:
        out["ManifestFilter"] = value["manifest_filter"]
    if "drm_settings" in value:
        out["DrmSettings"] = value["drm_settings"]
    if "start" in value:
        import aws_sdk_mediapackagev2.types._prelude.timestamp

        out["Start"] = aws_sdk_mediapackagev2.types._prelude.timestamp.serialize_json(
            value["start"]
        )
    if "end" in value:
        import aws_sdk_mediapackagev2.types._prelude.timestamp

        out["End"] = aws_sdk_mediapackagev2.types._prelude.timestamp.serialize_json(
            value["end"]
        )
    if "time_delay_seconds" in value:
        out["TimeDelaySeconds"] = value["time_delay_seconds"]
    if "clip_start_time" in value:
        import aws_sdk_mediapackagev2.types._prelude.timestamp

        out["ClipStartTime"] = (
            aws_sdk_mediapackagev2.types._prelude.timestamp.serialize_json(
                value["clip_start_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilterConfiguration:
    out: FilterConfiguration = {}  # type: ignore[typeddict-item]
    if "ManifestFilter" in data:
        out["manifest_filter"] = data["ManifestFilter"]
    if "DrmSettings" in data:
        out["drm_settings"] = data["DrmSettings"]
    if "Start" in data:
        import aws_sdk_mediapackagev2.types._prelude.timestamp

        out["start"] = aws_sdk_mediapackagev2.types._prelude.timestamp.deserialize_json(
            data["Start"]
        )
    if "End" in data:
        import aws_sdk_mediapackagev2.types._prelude.timestamp

        out["end"] = aws_sdk_mediapackagev2.types._prelude.timestamp.deserialize_json(
            data["End"]
        )
    if "TimeDelaySeconds" in data:
        out["time_delay_seconds"] = data["TimeDelaySeconds"]
    if "ClipStartTime" in data:
        import aws_sdk_mediapackagev2.types._prelude.timestamp

        out["clip_start_time"] = (
            aws_sdk_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["ClipStartTime"]
            )
        )
    return out
