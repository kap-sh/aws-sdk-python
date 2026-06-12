"""Generated from Smithy shape ``com.amazonaws.scheduler#FlexibleTimeWindow``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_scheduler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_scheduler.types.flexible_time_window_mode
    import aws_sdk_scheduler.types.maximum_window_in_minutes


class FlexibleTimeWindow(TypedDict):
    mode: "aws_sdk_scheduler.types.flexible_time_window_mode.FlexibleTimeWindowMode"
    """<p>Determines whether the schedule is invoked within a flexible time window.</p>"""
    maximum_window_in_minutes: NotRequired[
        "aws_sdk_scheduler.types.maximum_window_in_minutes.MaximumWindowInMinutes"
    ]
    """<p>The maximum time window during which a schedule can be invoked.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlexibleTimeWindow) -> dict:
    out: dict = {}
    out["Mode"] = value["mode"]
    if "maximum_window_in_minutes" in value:
        out["MaximumWindowInMinutes"] = value["maximum_window_in_minutes"]
    return out


def deserialize_json(data: dict) -> FlexibleTimeWindow:
    out: FlexibleTimeWindow = {}  # type: ignore[typeddict-item]
    if "Mode" in data:
        out["mode"] = data["Mode"]
    else:
        raise DeserializationError("FlexibleTimeWindow.mode required")
    if "MaximumWindowInMinutes" in data:
        out["maximum_window_in_minutes"] = data["MaximumWindowInMinutes"]
    return out
