"""Generated from Smithy shape ``com.amazonaws.location#BatchEvaluateGeofencesError``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.batch_item_error
    import aws_sdk_location.types.id
    import aws_sdk_location.types.timestamp


class BatchEvaluateGeofencesError(TypedDict):
    device_id: "aws_sdk_location.types.id.Id"
    """<p>The device associated with the position evaluation error.</p>"""
    sample_time: "aws_sdk_location.types.timestamp.Timestamp"
    r"""<p>Specifies a timestamp for when the error occurred in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""
    error: "aws_sdk_location.types.batch_item_error.BatchItemError"
    """<p>Contains details associated to the batch error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchEvaluateGeofencesError) -> dict:
    out: dict = {}
    out["DeviceId"] = value["device_id"]
    import aws_sdk_location.types.timestamp

    out["SampleTime"] = aws_sdk_location.types.timestamp.serialize_json(
        value["sample_time"]
    )
    import aws_sdk_location.types.batch_item_error

    out["Error"] = aws_sdk_location.types.batch_item_error.serialize_json(
        value["error"]
    )
    return out


def deserialize_json(data: dict) -> BatchEvaluateGeofencesError:
    out: BatchEvaluateGeofencesError = {}  # type: ignore[typeddict-item]
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    else:
        raise DeserializationError("BatchEvaluateGeofencesError.device_id required")
    if "SampleTime" in data:
        import aws_sdk_location.types.timestamp

        out["sample_time"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["SampleTime"]
        )
    else:
        raise DeserializationError("BatchEvaluateGeofencesError.sample_time required")
    if "Error" in data:
        import aws_sdk_location.types.batch_item_error

        out["error"] = aws_sdk_location.types.batch_item_error.deserialize_json(
            data["Error"]
        )
    else:
        raise DeserializationError("BatchEvaluateGeofencesError.error required")
    return out
