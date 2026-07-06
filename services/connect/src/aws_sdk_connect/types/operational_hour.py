"""Generated from Smithy shape ``com.amazonaws.connect#OperationalHour``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.override_time_slice


class OperationalHour(TypedDict, closed=True):
    start: NotRequired["aws_sdk_connect.types.override_time_slice.OverrideTimeSlice"]
    """<p>The start time that your contact center opens.</p>"""
    end: NotRequired["aws_sdk_connect.types.override_time_slice.OverrideTimeSlice"]
    """<p>The end time that your contact center closes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OperationalHour) -> dict:
    out: dict = {}
    if "start" in value:
        import aws_sdk_connect.types.override_time_slice

        out["Start"] = aws_sdk_connect.types.override_time_slice.serialize_json(
            value["start"]
        )
    if "end" in value:
        import aws_sdk_connect.types.override_time_slice

        out["End"] = aws_sdk_connect.types.override_time_slice.serialize_json(
            value["end"]
        )
    return out


def deserialize_json(data: dict) -> OperationalHour:
    out: OperationalHour = {}  # type: ignore[typeddict-item]
    if "Start" in data:
        import aws_sdk_connect.types.override_time_slice

        out["start"] = aws_sdk_connect.types.override_time_slice.deserialize_json(
            data["Start"]
        )
    if "End" in data:
        import aws_sdk_connect.types.override_time_slice

        out["end"] = aws_sdk_connect.types.override_time_slice.deserialize_json(
            data["End"]
        )
    return out
