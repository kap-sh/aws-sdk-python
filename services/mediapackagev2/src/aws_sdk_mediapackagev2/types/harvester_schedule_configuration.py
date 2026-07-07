"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#HarvesterScheduleConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class HarvesterScheduleConfiguration(TypedDict, closed=True):
    start_time: "datetime.datetime"
    """<p>The start time for the harvest job.</p>"""
    end_time: "datetime.datetime"
    """<p>The end time for the harvest job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarvesterScheduleConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_mediapackagev2.types._prelude.timestamp

    out["StartTime"] = aws_sdk_mediapackagev2.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    import aws_sdk_mediapackagev2.types._prelude.timestamp

    out["EndTime"] = aws_sdk_mediapackagev2.types._prelude.timestamp.serialize_json(
        value["end_time"]
    )
    return out


def deserialize_json(data: dict) -> HarvesterScheduleConfiguration:
    out: HarvesterScheduleConfiguration = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import aws_sdk_mediapackagev2.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    else:
        raise DeserializationError("HarvesterScheduleConfiguration.start_time required")
    if "EndTime" in data:
        import aws_sdk_mediapackagev2.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["EndTime"]
            )
        )
    else:
        raise DeserializationError("HarvesterScheduleConfiguration.end_time required")
    return out
