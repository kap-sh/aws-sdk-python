"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DataQualitySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lookoutequipment.types.duplicate_timestamps
    import capo_lookoutequipment.types.insufficient_sensor_data
    import capo_lookoutequipment.types.invalid_sensor_data
    import capo_lookoutequipment.types.missing_sensor_data
    import capo_lookoutequipment.types.unsupported_timestamps


class DataQualitySummary(TypedDict, closed=True):
    insufficient_sensor_data: (
        "capo_lookoutequipment.types.insufficient_sensor_data.InsufficientSensorData"
    )
    """<p> Parameter that gives information about insufficient data for sensors in the dataset. This includes information about those sensors that have complete data missing and those with a short date range. </p>"""
    missing_sensor_data: (
        "capo_lookoutequipment.types.missing_sensor_data.MissingSensorData"
    )
    """<p> Parameter that gives information about data that is missing over all the sensors in the input data. </p>"""
    invalid_sensor_data: (
        "capo_lookoutequipment.types.invalid_sensor_data.InvalidSensorData"
    )
    """<p> Parameter that gives information about data that is invalid over all the sensors in the input data. </p>"""
    unsupported_timestamps: (
        "capo_lookoutequipment.types.unsupported_timestamps.UnsupportedTimestamps"
    )
    """<p> Parameter that gives information about unsupported timestamps in the input data. </p>"""
    duplicate_timestamps: (
        "capo_lookoutequipment.types.duplicate_timestamps.DuplicateTimestamps"
    )
    """<p> Parameter that gives information about duplicate timestamps in the input data. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataQualitySummary) -> dict:
    out: dict = {}
    import capo_lookoutequipment.types.insufficient_sensor_data

    out["InsufficientSensorData"] = (
        capo_lookoutequipment.types.insufficient_sensor_data.serialize_aws_json_1_0(
            value["insufficient_sensor_data"]
        )
    )
    import capo_lookoutequipment.types.missing_sensor_data

    out["MissingSensorData"] = (
        capo_lookoutequipment.types.missing_sensor_data.serialize_aws_json_1_0(
            value["missing_sensor_data"]
        )
    )
    import capo_lookoutequipment.types.invalid_sensor_data

    out["InvalidSensorData"] = (
        capo_lookoutequipment.types.invalid_sensor_data.serialize_aws_json_1_0(
            value["invalid_sensor_data"]
        )
    )
    import capo_lookoutequipment.types.unsupported_timestamps

    out["UnsupportedTimestamps"] = (
        capo_lookoutequipment.types.unsupported_timestamps.serialize_aws_json_1_0(
            value["unsupported_timestamps"]
        )
    )
    import capo_lookoutequipment.types.duplicate_timestamps

    out["DuplicateTimestamps"] = (
        capo_lookoutequipment.types.duplicate_timestamps.serialize_aws_json_1_0(
            value["duplicate_timestamps"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DataQualitySummary:
    out: DataQualitySummary = {}  # type: ignore[typeddict-item]
    if "InsufficientSensorData" in data:
        import capo_lookoutequipment.types.insufficient_sensor_data

        out["insufficient_sensor_data"] = (
            capo_lookoutequipment.types.insufficient_sensor_data.deserialize_aws_json_1_0(
                data["InsufficientSensorData"]
            )
        )
    else:
        raise DeserializationError(
            "DataQualitySummary.insufficient_sensor_data required"
        )
    if "MissingSensorData" in data:
        import capo_lookoutequipment.types.missing_sensor_data

        out["missing_sensor_data"] = (
            capo_lookoutequipment.types.missing_sensor_data.deserialize_aws_json_1_0(
                data["MissingSensorData"]
            )
        )
    else:
        raise DeserializationError("DataQualitySummary.missing_sensor_data required")
    if "InvalidSensorData" in data:
        import capo_lookoutequipment.types.invalid_sensor_data

        out["invalid_sensor_data"] = (
            capo_lookoutequipment.types.invalid_sensor_data.deserialize_aws_json_1_0(
                data["InvalidSensorData"]
            )
        )
    else:
        raise DeserializationError("DataQualitySummary.invalid_sensor_data required")
    if "UnsupportedTimestamps" in data:
        import capo_lookoutequipment.types.unsupported_timestamps

        out["unsupported_timestamps"] = (
            capo_lookoutequipment.types.unsupported_timestamps.deserialize_aws_json_1_0(
                data["UnsupportedTimestamps"]
            )
        )
    else:
        raise DeserializationError("DataQualitySummary.unsupported_timestamps required")
    if "DuplicateTimestamps" in data:
        import capo_lookoutequipment.types.duplicate_timestamps

        out["duplicate_timestamps"] = (
            capo_lookoutequipment.types.duplicate_timestamps.deserialize_aws_json_1_0(
                data["DuplicateTimestamps"]
            )
        )
    else:
        raise DeserializationError("DataQualitySummary.duplicate_timestamps required")
    return out
