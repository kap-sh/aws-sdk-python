"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#SensorStatisticsSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.boolean
    import aws_sdk_lookoutequipment.types.categorical_values
    import aws_sdk_lookoutequipment.types.component_name
    import aws_sdk_lookoutequipment.types.count_percent
    import aws_sdk_lookoutequipment.types.large_timestamp_gaps
    import aws_sdk_lookoutequipment.types.monotonic_values
    import aws_sdk_lookoutequipment.types.multiple_operating_modes
    import aws_sdk_lookoutequipment.types.sensor_name
    import aws_sdk_lookoutequipment.types.timestamp


class SensorStatisticsSummary(TypedDict, closed=True):
    component_name: NotRequired[
        "aws_sdk_lookoutequipment.types.component_name.ComponentName"
    ]
    """<p> Name of the component to which the particular sensor belongs for which the statistics belong to. </p>"""
    sensor_name: NotRequired["aws_sdk_lookoutequipment.types.sensor_name.SensorName"]
    """<p> Name of the sensor that the statistics belong to. </p>"""
    data_exists: "aws_sdk_lookoutequipment.types.boolean.Boolean"
    """<p> Parameter that indicates whether data exists for the sensor that the statistics belong to. </p>"""
    missing_values: NotRequired[
        "aws_sdk_lookoutequipment.types.count_percent.CountPercent"
    ]
    """<p> Parameter that describes the total number of, and percentage of, values that are missing for the sensor that the statistics belong to. </p>"""
    invalid_values: NotRequired[
        "aws_sdk_lookoutequipment.types.count_percent.CountPercent"
    ]
    """<p> Parameter that describes the total number of, and percentage of, values that are invalid for the sensor that the statistics belong to. </p>"""
    invalid_date_entries: NotRequired[
        "aws_sdk_lookoutequipment.types.count_percent.CountPercent"
    ]
    """<p> Parameter that describes the total number of invalid date entries associated with the sensor that the statistics belong to. </p>"""
    duplicate_timestamps: NotRequired[
        "aws_sdk_lookoutequipment.types.count_percent.CountPercent"
    ]
    """<p> Parameter that describes the total number of duplicate timestamp records associated with the sensor that the statistics belong to. </p>"""
    categorical_values: NotRequired[
        "aws_sdk_lookoutequipment.types.categorical_values.CategoricalValues"
    ]
    """<p> Parameter that describes potential risk about whether data associated with the sensor is categorical. </p>"""
    multiple_operating_modes: NotRequired[
        "aws_sdk_lookoutequipment.types.multiple_operating_modes.MultipleOperatingModes"
    ]
    """<p> Parameter that describes potential risk about whether data associated with the sensor has more than one operating mode. </p>"""
    large_timestamp_gaps: NotRequired[
        "aws_sdk_lookoutequipment.types.large_timestamp_gaps.LargeTimestampGaps"
    ]
    """<p> Parameter that describes potential risk about whether data associated with the sensor contains one or more large gaps between consecutive timestamps. </p>"""
    monotonic_values: NotRequired[
        "aws_sdk_lookoutequipment.types.monotonic_values.MonotonicValues"
    ]
    """<p> Parameter that describes potential risk about whether data associated with the sensor is mostly monotonic. </p>"""
    data_start_time: NotRequired["aws_sdk_lookoutequipment.types.timestamp.Timestamp"]
    """<p> Indicates the time reference to indicate the beginning of valid data associated with the sensor that the statistics belong to. </p>"""
    data_end_time: NotRequired["aws_sdk_lookoutequipment.types.timestamp.Timestamp"]
    """<p> Indicates the time reference to indicate the end of valid data associated with the sensor that the statistics belong to. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SensorStatisticsSummary) -> dict:
    out: dict = {}
    if "component_name" in value:
        out["ComponentName"] = value["component_name"]
    if "sensor_name" in value:
        out["SensorName"] = value["sensor_name"]
    out["DataExists"] = value.get("data_exists", False)
    if "missing_values" in value:
        import aws_sdk_lookoutequipment.types.count_percent

        out["MissingValues"] = (
            aws_sdk_lookoutequipment.types.count_percent.serialize_aws_json_1_0(
                value["missing_values"]
            )
        )
    if "invalid_values" in value:
        import aws_sdk_lookoutequipment.types.count_percent

        out["InvalidValues"] = (
            aws_sdk_lookoutequipment.types.count_percent.serialize_aws_json_1_0(
                value["invalid_values"]
            )
        )
    if "invalid_date_entries" in value:
        import aws_sdk_lookoutequipment.types.count_percent

        out["InvalidDateEntries"] = (
            aws_sdk_lookoutequipment.types.count_percent.serialize_aws_json_1_0(
                value["invalid_date_entries"]
            )
        )
    if "duplicate_timestamps" in value:
        import aws_sdk_lookoutequipment.types.count_percent

        out["DuplicateTimestamps"] = (
            aws_sdk_lookoutequipment.types.count_percent.serialize_aws_json_1_0(
                value["duplicate_timestamps"]
            )
        )
    if "categorical_values" in value:
        import aws_sdk_lookoutequipment.types.categorical_values

        out["CategoricalValues"] = (
            aws_sdk_lookoutequipment.types.categorical_values.serialize_aws_json_1_0(
                value["categorical_values"]
            )
        )
    if "multiple_operating_modes" in value:
        import aws_sdk_lookoutequipment.types.multiple_operating_modes

        out["MultipleOperatingModes"] = (
            aws_sdk_lookoutequipment.types.multiple_operating_modes.serialize_aws_json_1_0(
                value["multiple_operating_modes"]
            )
        )
    if "large_timestamp_gaps" in value:
        import aws_sdk_lookoutequipment.types.large_timestamp_gaps

        out["LargeTimestampGaps"] = (
            aws_sdk_lookoutequipment.types.large_timestamp_gaps.serialize_aws_json_1_0(
                value["large_timestamp_gaps"]
            )
        )
    if "monotonic_values" in value:
        import aws_sdk_lookoutequipment.types.monotonic_values

        out["MonotonicValues"] = (
            aws_sdk_lookoutequipment.types.monotonic_values.serialize_aws_json_1_0(
                value["monotonic_values"]
            )
        )
    if "data_start_time" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["DataStartTime"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["data_start_time"]
            )
        )
    if "data_end_time" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["DataEndTime"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["data_end_time"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SensorStatisticsSummary:
    out: SensorStatisticsSummary = {}  # type: ignore[typeddict-item]
    if "ComponentName" in data:
        out["component_name"] = data["ComponentName"]
    if "SensorName" in data:
        out["sensor_name"] = data["SensorName"]
    if "DataExists" in data:
        out["data_exists"] = data["DataExists"]
    else:
        out["data_exists"] = False
    if "MissingValues" in data:
        import aws_sdk_lookoutequipment.types.count_percent

        out["missing_values"] = (
            aws_sdk_lookoutequipment.types.count_percent.deserialize_aws_json_1_0(
                data["MissingValues"]
            )
        )
    if "InvalidValues" in data:
        import aws_sdk_lookoutequipment.types.count_percent

        out["invalid_values"] = (
            aws_sdk_lookoutequipment.types.count_percent.deserialize_aws_json_1_0(
                data["InvalidValues"]
            )
        )
    if "InvalidDateEntries" in data:
        import aws_sdk_lookoutequipment.types.count_percent

        out["invalid_date_entries"] = (
            aws_sdk_lookoutequipment.types.count_percent.deserialize_aws_json_1_0(
                data["InvalidDateEntries"]
            )
        )
    if "DuplicateTimestamps" in data:
        import aws_sdk_lookoutequipment.types.count_percent

        out["duplicate_timestamps"] = (
            aws_sdk_lookoutequipment.types.count_percent.deserialize_aws_json_1_0(
                data["DuplicateTimestamps"]
            )
        )
    if "CategoricalValues" in data:
        import aws_sdk_lookoutequipment.types.categorical_values

        out["categorical_values"] = (
            aws_sdk_lookoutequipment.types.categorical_values.deserialize_aws_json_1_0(
                data["CategoricalValues"]
            )
        )
    if "MultipleOperatingModes" in data:
        import aws_sdk_lookoutequipment.types.multiple_operating_modes

        out["multiple_operating_modes"] = (
            aws_sdk_lookoutequipment.types.multiple_operating_modes.deserialize_aws_json_1_0(
                data["MultipleOperatingModes"]
            )
        )
    if "LargeTimestampGaps" in data:
        import aws_sdk_lookoutequipment.types.large_timestamp_gaps

        out["large_timestamp_gaps"] = (
            aws_sdk_lookoutequipment.types.large_timestamp_gaps.deserialize_aws_json_1_0(
                data["LargeTimestampGaps"]
            )
        )
    if "MonotonicValues" in data:
        import aws_sdk_lookoutequipment.types.monotonic_values

        out["monotonic_values"] = (
            aws_sdk_lookoutequipment.types.monotonic_values.deserialize_aws_json_1_0(
                data["MonotonicValues"]
            )
        )
    if "DataStartTime" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["data_start_time"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["DataStartTime"]
            )
        )
    if "DataEndTime" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["data_end_time"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["DataEndTime"]
            )
        )
    return out
