"""Generated from Smithy shape ``com.amazonaws.pi#DataPoint``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pi.types.double
    import aws_sdk_pi.types.iso_timestamp


class DataPoint(TypedDict):
    timestamp: "aws_sdk_pi.types.iso_timestamp.ISOTimestamp"
    """<p>The time, in epoch format, associated with a particular <code>Value</code>.</p>"""
    value: "aws_sdk_pi.types.double.Double"
    """<p>The actual value associated with a particular <code>Timestamp</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataPoint) -> dict:
    out: dict = {}
    import aws_sdk_pi.types.iso_timestamp

    out["Timestamp"] = aws_sdk_pi.types.iso_timestamp.serialize_aws_json_1_1(
        value["timestamp"]
    )
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataPoint:
    out: DataPoint = {}  # type: ignore[typeddict-item]
    if "Timestamp" in data:
        import aws_sdk_pi.types.iso_timestamp

        out["timestamp"] = aws_sdk_pi.types.iso_timestamp.deserialize_aws_json_1_1(
            data["Timestamp"]
        )
    else:
        raise DeserializationError("DataPoint.timestamp required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("DataPoint.value required")
    return out
