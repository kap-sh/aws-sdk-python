"""Generated from Smithy shape ``com.amazonaws.opensearch#OffPeakWindow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.window_start_time


class OffPeakWindow(TypedDict, closed=True):
    window_start_time: NotRequired[
        "capo_opensearch.types.window_start_time.WindowStartTime"
    ]
    """<p>A custom start time for the off-peak window, in Coordinated Universal Time (UTC). The window length will always be 10 hours, so you can't specify an end time. For example, if you specify 11:00 P.M. UTC as a start time, the end time will automatically be set to 9:00 A.M.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OffPeakWindow) -> dict:
    out: dict = {}
    if "window_start_time" in value:
        import capo_opensearch.types.window_start_time

        out["WindowStartTime"] = capo_opensearch.types.window_start_time.serialize_json(
            value["window_start_time"]
        )
    return out


def deserialize_json(data: dict) -> OffPeakWindow:
    out: OffPeakWindow = {}  # type: ignore[typeddict-item]
    if "WindowStartTime" in data:
        import capo_opensearch.types.window_start_time

        out["window_start_time"] = (
            capo_opensearch.types.window_start_time.deserialize_json(
                data["WindowStartTime"]
            )
        )
    return out
