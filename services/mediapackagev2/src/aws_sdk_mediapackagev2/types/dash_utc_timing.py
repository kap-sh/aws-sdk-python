"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashUtcTiming``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.dash_utc_timing_mode


class DashUtcTiming(TypedDict, closed=True):
    timing_mode: NotRequired[
        "aws_sdk_mediapackagev2.types.dash_utc_timing_mode.DashUtcTimingMode"
    ]
    """<p>The UTC timing mode.</p>"""
    timing_source: NotRequired["str"]
    """<p>The the method that the player uses to synchronize to coordinated universal time (UTC) wall clock time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashUtcTiming) -> dict:
    out: dict = {}
    if "timing_mode" in value:
        import aws_sdk_mediapackagev2.types.dash_utc_timing_mode

        out["TimingMode"] = (
            aws_sdk_mediapackagev2.types.dash_utc_timing_mode.serialize_json(
                value["timing_mode"]
            )
        )
    if "timing_source" in value:
        out["TimingSource"] = value["timing_source"]
    return out


def deserialize_json(data: dict) -> DashUtcTiming:
    out: DashUtcTiming = {}  # type: ignore[typeddict-item]
    if "TimingMode" in data:
        import aws_sdk_mediapackagev2.types.dash_utc_timing_mode

        out["timing_mode"] = (
            aws_sdk_mediapackagev2.types.dash_utc_timing_mode.deserialize_json(
                data["TimingMode"]
            )
        )
    if "TimingSource" in data:
        out["timing_source"] = data["TimingSource"]
    return out
