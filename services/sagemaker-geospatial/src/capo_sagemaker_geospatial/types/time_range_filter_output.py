"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#TimeRangeFilterOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class TimeRangeFilterOutput(TypedDict, closed=True):
    start_time: "datetime.datetime"
    """<p>The starting time for the time range filter.</p>"""
    end_time: "datetime.datetime"
    """<p>The ending time for the time range filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeRangeFilterOutput) -> dict:
    out: dict = {}
    import capo_sagemaker_geospatial.types._prelude.timestamp

    out["StartTime"] = (
        capo_sagemaker_geospatial.types._prelude.timestamp.serialize_json(
            value["start_time"]
        )
    )
    import capo_sagemaker_geospatial.types._prelude.timestamp

    out["EndTime"] = capo_sagemaker_geospatial.types._prelude.timestamp.serialize_json(
        value["end_time"]
    )
    return out


def deserialize_json(data: dict) -> TimeRangeFilterOutput:
    out: TimeRangeFilterOutput = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import capo_sagemaker_geospatial.types._prelude.timestamp

        out["start_time"] = (
            capo_sagemaker_geospatial.types._prelude.timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    else:
        raise DeserializationError("TimeRangeFilterOutput.start_time required")
    if "EndTime" in data:
        import capo_sagemaker_geospatial.types._prelude.timestamp

        out["end_time"] = (
            capo_sagemaker_geospatial.types._prelude.timestamp.deserialize_json(
                data["EndTime"]
            )
        )
    else:
        raise DeserializationError("TimeRangeFilterOutput.end_time required")
    return out
