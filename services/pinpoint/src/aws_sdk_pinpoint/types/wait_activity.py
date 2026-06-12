"""Generated from Smithy shape ``com.amazonaws.pinpoint#WaitActivity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.wait_time


class WaitActivity(TypedDict):
    next_activity: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the next activity to perform, after performing the wait activity.</p>"""
    wait_time: NotRequired["aws_sdk_pinpoint.types.wait_time.WaitTime"]
    """<p>The amount of time to wait or the date and time when the activity moves participants to the next activity in the journey.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaitActivity) -> dict:
    out: dict = {}
    if "next_activity" in value:
        out["NextActivity"] = value["next_activity"]
    if "wait_time" in value:
        import aws_sdk_pinpoint.types.wait_time

        out["WaitTime"] = aws_sdk_pinpoint.types.wait_time.serialize_json(
            value["wait_time"]
        )
    return out


def deserialize_json(data: dict) -> WaitActivity:
    out: WaitActivity = {}  # type: ignore[typeddict-item]
    if "NextActivity" in data:
        out["next_activity"] = data["NextActivity"]
    if "WaitTime" in data:
        import aws_sdk_pinpoint.types.wait_time

        out["wait_time"] = aws_sdk_pinpoint.types.wait_time.deserialize_json(
            data["WaitTime"]
        )
    return out
