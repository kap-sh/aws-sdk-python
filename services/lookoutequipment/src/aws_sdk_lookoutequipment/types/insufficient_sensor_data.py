"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#InsufficientSensorData``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.missing_complete_sensor_data
    import aws_sdk_lookoutequipment.types.sensors_with_short_date_range


class InsufficientSensorData(TypedDict, closed=True):
    missing_complete_sensor_data: "aws_sdk_lookoutequipment.types.missing_complete_sensor_data.MissingCompleteSensorData"
    """<p> Parameter that describes the total number of sensors that have data completely missing for it. </p>"""
    sensors_with_short_date_range: "aws_sdk_lookoutequipment.types.sensors_with_short_date_range.SensorsWithShortDateRange"
    """<p> Parameter that describes the total number of sensors that have a short date range of less than 14 days of data overall. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InsufficientSensorData) -> dict:
    out: dict = {}
    import aws_sdk_lookoutequipment.types.missing_complete_sensor_data

    out["MissingCompleteSensorData"] = (
        aws_sdk_lookoutequipment.types.missing_complete_sensor_data.serialize_aws_json_1_0(
            value["missing_complete_sensor_data"]
        )
    )
    import aws_sdk_lookoutequipment.types.sensors_with_short_date_range

    out["SensorsWithShortDateRange"] = (
        aws_sdk_lookoutequipment.types.sensors_with_short_date_range.serialize_aws_json_1_0(
            value["sensors_with_short_date_range"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> InsufficientSensorData:
    out: InsufficientSensorData = {}  # type: ignore[typeddict-item]
    if "MissingCompleteSensorData" in data:
        import aws_sdk_lookoutequipment.types.missing_complete_sensor_data

        out["missing_complete_sensor_data"] = (
            aws_sdk_lookoutequipment.types.missing_complete_sensor_data.deserialize_aws_json_1_0(
                data["MissingCompleteSensorData"]
            )
        )
    else:
        raise DeserializationError(
            "InsufficientSensorData.missing_complete_sensor_data required"
        )
    if "SensorsWithShortDateRange" in data:
        import aws_sdk_lookoutequipment.types.sensors_with_short_date_range

        out["sensors_with_short_date_range"] = (
            aws_sdk_lookoutequipment.types.sensors_with_short_date_range.deserialize_aws_json_1_0(
                data["SensorsWithShortDateRange"]
            )
        )
    else:
        raise DeserializationError(
            "InsufficientSensorData.sensors_with_short_date_range required"
        )
    return out
