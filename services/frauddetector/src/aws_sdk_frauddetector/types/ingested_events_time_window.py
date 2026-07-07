"""Generated from Smithy shape ``com.amazonaws.frauddetector#IngestedEventsTimeWindow``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.time


class IngestedEventsTimeWindow(TypedDict, closed=True):
    start_time: "aws_sdk_frauddetector.types.time.time"
    """<p>Timestamp of the first ingensted event.</p>"""
    end_time: "aws_sdk_frauddetector.types.time.time"
    """<p>Timestamp of the final ingested event.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IngestedEventsTimeWindow) -> dict:
    out: dict = {}
    out["startTime"] = value["start_time"]
    out["endTime"] = value["end_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IngestedEventsTimeWindow:
    out: IngestedEventsTimeWindow = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        out["start_time"] = data["startTime"]
    else:
        raise DeserializationError("IngestedEventsTimeWindow.start_time required")
    if "endTime" in data:
        out["end_time"] = data["endTime"]
    else:
        raise DeserializationError("IngestedEventsTimeWindow.end_time required")
    return out
