"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#MissingCompleteSensorData``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.integer


class MissingCompleteSensorData(TypedDict):
    affected_sensor_count: "aws_sdk_lookoutequipment.types.integer.Integer"
    """<p> Indicates the number of sensors that have data missing completely. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MissingCompleteSensorData) -> dict:
    out: dict = {}
    out["AffectedSensorCount"] = value["affected_sensor_count"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MissingCompleteSensorData:
    out: MissingCompleteSensorData = {}  # type: ignore[typeddict-item]
    if "AffectedSensorCount" in data:
        out["affected_sensor_count"] = data["AffectedSensorCount"]
    else:
        raise DeserializationError(
            "MissingCompleteSensorData.affected_sensor_count required"
        )
    return out
