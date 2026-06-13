"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#TimeRangeFilterInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class TimeRangeFilterInput(TypedDict):
    start_time: "datetime.datetime"
    """<p>The start time for the time-range filter.</p>"""
    end_time: "datetime.datetime"
    """<p>The end time for the time-range filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeRangeFilterInput) -> dict:
    out: dict = {}
    import aws_sdk_sagemaker_geospatial.types._prelude.timestamp

    out["StartTime"] = (
        aws_sdk_sagemaker_geospatial.types._prelude.timestamp.serialize_json(
            value["start_time"]
        )
    )
    import aws_sdk_sagemaker_geospatial.types._prelude.timestamp

    out["EndTime"] = (
        aws_sdk_sagemaker_geospatial.types._prelude.timestamp.serialize_json(
            value["end_time"]
        )
    )
    return out


def deserialize_json(data: dict) -> TimeRangeFilterInput:
    out: TimeRangeFilterInput = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import aws_sdk_sagemaker_geospatial.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_sagemaker_geospatial.types._prelude.timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    else:
        raise DeserializationError("TimeRangeFilterInput.start_time required")
    if "EndTime" in data:
        import aws_sdk_sagemaker_geospatial.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_sagemaker_geospatial.types._prelude.timestamp.deserialize_json(
                data["EndTime"]
            )
        )
    else:
        raise DeserializationError("TimeRangeFilterInput.end_time required")
    return out
