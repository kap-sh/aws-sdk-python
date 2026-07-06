"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#Duration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_timestream_influxdb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_influxdb.types.duration_type


class Duration(TypedDict, closed=True):
    duration_type: "aws_sdk_timestream_influxdb.types.duration_type.DurationType"
    """<p>The type of duration for InfluxDB parameters.</p>"""
    value: "int"
    """<p>The value of duration for InfluxDB parameters.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Duration) -> dict:
    out: dict = {}
    import aws_sdk_timestream_influxdb.types.duration_type

    out["durationType"] = (
        aws_sdk_timestream_influxdb.types.duration_type.serialize_aws_json_1_0(
            value["duration_type"]
        )
    )
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Duration:
    out: Duration = {}  # type: ignore[typeddict-item]
    if "durationType" in data:
        import aws_sdk_timestream_influxdb.types.duration_type

        out["duration_type"] = (
            aws_sdk_timestream_influxdb.types.duration_type.deserialize_aws_json_1_0(
                data["durationType"]
            )
        )
    else:
        raise DeserializationError("Duration.duration_type required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("Duration.value required")
    return out
