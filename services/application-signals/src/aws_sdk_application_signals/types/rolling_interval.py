"""Generated from Smithy shape ``com.amazonaws.applicationsignals#RollingInterval``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.duration_unit
    import aws_sdk_application_signals.types.rolling_interval_duration


class RollingInterval(TypedDict):
    duration_unit: "aws_sdk_application_signals.types.duration_unit.DurationUnit"
    """<p>Specifies the rolling interval unit.</p>"""
    duration: "aws_sdk_application_signals.types.rolling_interval_duration.RollingIntervalDuration"
    """<p>Specifies the duration of each rolling interval. For example, if <code>Duration</code> is <code>7</code> and <code>DurationUnit</code> is <code>DAY</code>, each rolling interval is seven days.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RollingInterval) -> dict:
    out: dict = {}
    import aws_sdk_application_signals.types.duration_unit

    out["DurationUnit"] = (
        aws_sdk_application_signals.types.duration_unit.serialize_json(
            value["duration_unit"]
        )
    )
    out["Duration"] = value["duration"]
    return out


def deserialize_json(data: dict) -> RollingInterval:
    out: RollingInterval = {}  # type: ignore[typeddict-item]
    if "DurationUnit" in data:
        import aws_sdk_application_signals.types.duration_unit

        out["duration_unit"] = (
            aws_sdk_application_signals.types.duration_unit.deserialize_json(
                data["DurationUnit"]
            )
        )
    else:
        raise DeserializationError("RollingInterval.duration_unit required")
    if "Duration" in data:
        out["duration"] = data["Duration"]
    else:
        raise DeserializationError("RollingInterval.duration required")
    return out
