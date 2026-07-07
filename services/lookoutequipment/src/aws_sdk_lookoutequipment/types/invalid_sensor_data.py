"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#InvalidSensorData``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.integer


class InvalidSensorData(TypedDict, closed=True):
    affected_sensor_count: "aws_sdk_lookoutequipment.types.integer.Integer"
    """<p> Indicates the number of sensors that have at least some invalid values. </p>"""
    total_number_of_invalid_values: "aws_sdk_lookoutequipment.types.integer.Integer"
    """<p> Indicates the total number of invalid values across all the sensors. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvalidSensorData) -> dict:
    out: dict = {}
    out["AffectedSensorCount"] = value["affected_sensor_count"]
    out["TotalNumberOfInvalidValues"] = value["total_number_of_invalid_values"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InvalidSensorData:
    out: InvalidSensorData = {}  # type: ignore[typeddict-item]
    if "AffectedSensorCount" in data:
        out["affected_sensor_count"] = data["AffectedSensorCount"]
    else:
        raise DeserializationError("InvalidSensorData.affected_sensor_count required")
    if "TotalNumberOfInvalidValues" in data:
        out["total_number_of_invalid_values"] = data["TotalNumberOfInvalidValues"]
    else:
        raise DeserializationError(
            "InvalidSensorData.total_number_of_invalid_values required"
        )
    return out
