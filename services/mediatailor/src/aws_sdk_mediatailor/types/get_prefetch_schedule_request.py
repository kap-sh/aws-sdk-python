"""Generated from Smithy shape ``com.amazonaws.mediatailor#GetPrefetchScheduleRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string


class GetPrefetchScheduleRequest(TypedDict):
    name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the prefetch schedule. The name must be unique among all prefetch schedules that are associated with the specified playback configuration.</p>"""
    playback_configuration_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>Returns information about the prefetch schedule for a specific playback configuration. If you call <code>GetPrefetchSchedule</code> on an expired prefetch schedule, MediaTailor returns an HTTP 404 status code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPrefetchScheduleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPrefetchScheduleRequest:
    out: GetPrefetchScheduleRequest = {}  # type: ignore[typeddict-item]
    return out
