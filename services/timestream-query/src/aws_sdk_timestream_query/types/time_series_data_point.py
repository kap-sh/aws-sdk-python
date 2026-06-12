"""Generated from Smithy shape ``com.amazonaws.timestreamquery#TimeSeriesDataPoint``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.datum
    import aws_sdk_timestream_query.types.timestamp


class TimeSeriesDataPoint(TypedDict):
    time: "aws_sdk_timestream_query.types.timestamp.Timestamp"
    """<p>The timestamp when the measure value was collected.</p>"""
    value: "aws_sdk_timestream_query.types.datum.Datum"
    """<p>The measure value for the data point.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimeSeriesDataPoint) -> dict:
    out: dict = {}
    out["Time"] = value["time"]
    import aws_sdk_timestream_query.types.datum

    out["Value"] = aws_sdk_timestream_query.types.datum.serialize_aws_json_1_0(
        value["value"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TimeSeriesDataPoint:
    out: TimeSeriesDataPoint = {}  # type: ignore[typeddict-item]
    if "Time" in data:
        out["time"] = data["Time"]
    else:
        raise DeserializationError("TimeSeriesDataPoint.time required")
    if "Value" in data:
        import aws_sdk_timestream_query.types.datum

        out["value"] = aws_sdk_timestream_query.types.datum.deserialize_aws_json_1_0(
            data["Value"]
        )
    else:
        raise DeserializationError("TimeSeriesDataPoint.value required")
    return out
