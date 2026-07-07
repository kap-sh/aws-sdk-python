"""Generated from Smithy shape ``com.amazonaws.connect#RecurrenceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.recurrence_pattern


class RecurrenceConfig(TypedDict, closed=True):
    recurrence_pattern: "aws_sdk_connect.types.recurrence_pattern.RecurrencePattern"
    """<p>The recurrence pattern that defines how the event repeats. Example: Frequency, Interval, ByMonth, ByMonthDay, ByWeekdayOccurrence</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecurrenceConfig) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.recurrence_pattern

    out["RecurrencePattern"] = aws_sdk_connect.types.recurrence_pattern.serialize_json(
        value["recurrence_pattern"]
    )
    return out


def deserialize_json(data: dict) -> RecurrenceConfig:
    out: RecurrenceConfig = {}  # type: ignore[typeddict-item]
    if "RecurrencePattern" in data:
        import aws_sdk_connect.types.recurrence_pattern

        out["recurrence_pattern"] = (
            aws_sdk_connect.types.recurrence_pattern.deserialize_json(
                data["RecurrencePattern"]
            )
        )
    else:
        raise DeserializationError("RecurrenceConfig.recurrence_pattern required")
    return out
