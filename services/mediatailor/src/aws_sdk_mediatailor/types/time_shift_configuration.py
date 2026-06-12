"""Generated from Smithy shape ``com.amazonaws.mediatailor#TimeShiftConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__integer


class TimeShiftConfiguration(TypedDict):
    max_time_delay_seconds: "aws_sdk_mediatailor.types.__integer.__integer"
    """<p> The maximum time delay for time-shifted viewing. The minimum allowed maximum time delay is 0 seconds, and the maximum allowed maximum time delay is 21600 seconds (6 hours). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeShiftConfiguration) -> dict:
    out: dict = {}
    out["MaxTimeDelaySeconds"] = value["max_time_delay_seconds"]
    return out


def deserialize_json(data: dict) -> TimeShiftConfiguration:
    out: TimeShiftConfiguration = {}  # type: ignore[typeddict-item]
    if "MaxTimeDelaySeconds" in data:
        out["max_time_delay_seconds"] = data["MaxTimeDelaySeconds"]
    else:
        raise DeserializationError(
            "TimeShiftConfiguration.max_time_delay_seconds required"
        )
    return out
