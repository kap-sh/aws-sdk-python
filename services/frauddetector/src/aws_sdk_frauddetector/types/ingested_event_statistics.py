"""Generated from Smithy shape ``com.amazonaws.frauddetector#IngestedEventStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.long
    import aws_sdk_frauddetector.types.time


class IngestedEventStatistics(TypedDict, closed=True):
    number_of_events: NotRequired["aws_sdk_frauddetector.types.long.Long"]
    """<p>The number of stored events.</p>"""
    event_data_size_in_bytes: NotRequired["aws_sdk_frauddetector.types.long.Long"]
    """<p>The total size of the stored events.</p>"""
    least_recent_event: NotRequired["aws_sdk_frauddetector.types.time.time"]
    """<p>The oldest stored event.</p>"""
    most_recent_event: NotRequired["aws_sdk_frauddetector.types.time.time"]
    """<p>The newest stored event.</p>"""
    last_updated_time: NotRequired["aws_sdk_frauddetector.types.time.time"]
    """<p>Timestamp of when the stored event was last updated. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IngestedEventStatistics) -> dict:
    out: dict = {}
    if "number_of_events" in value:
        out["numberOfEvents"] = value["number_of_events"]
    if "event_data_size_in_bytes" in value:
        out["eventDataSizeInBytes"] = value["event_data_size_in_bytes"]
    if "least_recent_event" in value:
        out["leastRecentEvent"] = value["least_recent_event"]
    if "most_recent_event" in value:
        out["mostRecentEvent"] = value["most_recent_event"]
    if "last_updated_time" in value:
        out["lastUpdatedTime"] = value["last_updated_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IngestedEventStatistics:
    out: IngestedEventStatistics = {}  # type: ignore[typeddict-item]
    if "numberOfEvents" in data:
        out["number_of_events"] = data["numberOfEvents"]
    if "eventDataSizeInBytes" in data:
        out["event_data_size_in_bytes"] = data["eventDataSizeInBytes"]
    if "leastRecentEvent" in data:
        out["least_recent_event"] = data["leastRecentEvent"]
    if "mostRecentEvent" in data:
        out["most_recent_event"] = data["mostRecentEvent"]
    if "lastUpdatedTime" in data:
        out["last_updated_time"] = data["lastUpdatedTime"]
    return out
