"""Generated from Smithy shape ``com.amazonaws.mediatailor#DashPlaylistSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__integer


class DashPlaylistSettings(TypedDict):
    manifest_window_seconds: NotRequired[
        "aws_sdk_mediatailor.types.__integer.__integer"
    ]
    """<p>The total duration (in seconds) of each manifest. Minimum value: <code>30</code> seconds. Maximum value: <code>3600</code> seconds.</p>"""
    min_buffer_time_seconds: NotRequired[
        "aws_sdk_mediatailor.types.__integer.__integer"
    ]
    """<p>Minimum amount of content (measured in seconds) that a player must keep available in the buffer. Minimum value: <code>2</code> seconds. Maximum value: <code>60</code> seconds.</p>"""
    min_update_period_seconds: NotRequired[
        "aws_sdk_mediatailor.types.__integer.__integer"
    ]
    """<p>Minimum amount of time (in seconds) that the player should wait before requesting updates to the manifest. Minimum value: <code>2</code> seconds. Maximum value: <code>60</code> seconds.</p>"""
    suggested_presentation_delay_seconds: NotRequired[
        "aws_sdk_mediatailor.types.__integer.__integer"
    ]
    """<p>Amount of time (in seconds) that the player should be from the live point at the end of the manifest. Minimum value: <code>2</code> seconds. Maximum value: <code>60</code> seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashPlaylistSettings) -> dict:
    out: dict = {}
    if "manifest_window_seconds" in value:
        out["ManifestWindowSeconds"] = value["manifest_window_seconds"]
    if "min_buffer_time_seconds" in value:
        out["MinBufferTimeSeconds"] = value["min_buffer_time_seconds"]
    if "min_update_period_seconds" in value:
        out["MinUpdatePeriodSeconds"] = value["min_update_period_seconds"]
    if "suggested_presentation_delay_seconds" in value:
        out["SuggestedPresentationDelaySeconds"] = value[
            "suggested_presentation_delay_seconds"
        ]
    return out


def deserialize_json(data: dict) -> DashPlaylistSettings:
    out: DashPlaylistSettings = {}  # type: ignore[typeddict-item]
    if "ManifestWindowSeconds" in data:
        out["manifest_window_seconds"] = data["ManifestWindowSeconds"]
    if "MinBufferTimeSeconds" in data:
        out["min_buffer_time_seconds"] = data["MinBufferTimeSeconds"]
    if "MinUpdatePeriodSeconds" in data:
        out["min_update_period_seconds"] = data["MinUpdatePeriodSeconds"]
    if "SuggestedPresentationDelaySeconds" in data:
        out["suggested_presentation_delay_seconds"] = data[
            "SuggestedPresentationDelaySeconds"
        ]
    return out
