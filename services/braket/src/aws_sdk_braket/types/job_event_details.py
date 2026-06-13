"""Generated from Smithy shape ``com.amazonaws.braket#JobEventDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_braket.types.job_event_type


class JobEventDetails(TypedDict):
    event_type: NotRequired["aws_sdk_braket.types.job_event_type.JobEventType"]
    """<p>The type of event that occurred related to the Amazon Braket hybrid job.</p>"""
    time_of_event: NotRequired["datetime.datetime"]
    """<p>The time of the event that occurred related to the Amazon Braket hybrid job.</p>"""
    message: NotRequired["str"]
    """<p>A message describing the event that occurred related to the Amazon Braket hybrid job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobEventDetails) -> dict:
    out: dict = {}
    if "event_type" in value:
        out["eventType"] = value["event_type"]
    if "time_of_event" in value:
        import aws_sdk_braket.types._prelude.timestamp

        out["timeOfEvent"] = aws_sdk_braket.types._prelude.timestamp.serialize_json(
            value["time_of_event"]
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> JobEventDetails:
    out: JobEventDetails = {}  # type: ignore[typeddict-item]
    if "eventType" in data:
        out["event_type"] = data["eventType"]
    if "timeOfEvent" in data:
        import aws_sdk_braket.types._prelude.timestamp

        out["time_of_event"] = aws_sdk_braket.types._prelude.timestamp.deserialize_json(
            data["timeOfEvent"]
        )
    if "message" in data:
        out["message"] = data["message"]
    return out
