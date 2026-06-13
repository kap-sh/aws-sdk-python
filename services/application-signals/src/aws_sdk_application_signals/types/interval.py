"""Generated from Smithy shape ``com.amazonaws.applicationsignals#Interval``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_application_signals.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.calendar_interval
    import aws_sdk_application_signals.types.rolling_interval


class _Interval_RollingInterval(TypedDict):
    RollingInterval: (
        "aws_sdk_application_signals.types.rolling_interval.RollingInterval"
    )


class _Interval_CalendarInterval(TypedDict):
    CalendarInterval: (
        "aws_sdk_application_signals.types.calendar_interval.CalendarInterval"
    )


Interval: TypeAlias = _Interval_RollingInterval | _Interval_CalendarInterval


# --- restJson1 ser/de ---
def serialize_json(value: Interval) -> dict:
    if "RollingInterval" in value:
        import aws_sdk_application_signals.types.rolling_interval

        return {
            "RollingInterval": aws_sdk_application_signals.types.rolling_interval.serialize_json(
                value["RollingInterval"]
            )
        }
    elif "CalendarInterval" in value:
        import aws_sdk_application_signals.types.calendar_interval

        return {
            "CalendarInterval": aws_sdk_application_signals.types.calendar_interval.serialize_json(
                value["CalendarInterval"]
            )
        }
    else:
        raise SerializationError("Interval: no variant present")


def deserialize_json(data: dict) -> Interval:
    if "RollingInterval" in data:
        import aws_sdk_application_signals.types.rolling_interval

        return {
            "RollingInterval": aws_sdk_application_signals.types.rolling_interval.deserialize_json(
                data["RollingInterval"]
            )
        }
    elif "CalendarInterval" in data:
        import aws_sdk_application_signals.types.calendar_interval

        return {
            "CalendarInterval": aws_sdk_application_signals.types.calendar_interval.deserialize_json(
                data["CalendarInterval"]
            )
        }
    else:
        raise DeserializationError("Interval: no recognized variant key")
