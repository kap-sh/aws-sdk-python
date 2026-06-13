"""Generated from Smithy shape ``com.amazonaws.quicksight#DateTimeDatasetParameter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dataset_parameter_id
    import aws_sdk_quicksight.types.dataset_parameter_name
    import aws_sdk_quicksight.types.dataset_parameter_value_type
    import aws_sdk_quicksight.types.date_time_dataset_parameter_default_values
    import aws_sdk_quicksight.types.time_granularity


class DateTimeDatasetParameter(TypedDict):
    id: "aws_sdk_quicksight.types.dataset_parameter_id.DatasetParameterId"
    """<p>An identifier for the parameter that is created in the dataset.</p>"""
    name: "aws_sdk_quicksight.types.dataset_parameter_name.DatasetParameterName"
    """<p>The name of the date time parameter that is created in the dataset.</p>"""
    value_type: "aws_sdk_quicksight.types.dataset_parameter_value_type.DatasetParameterValueType"
    """<p>The value type of the dataset parameter. Valid values are <code>single value</code> or <code>multi value</code>.</p>"""
    time_granularity: NotRequired[
        "aws_sdk_quicksight.types.time_granularity.TimeGranularity"
    ]
    """<p>The time granularity of the date time parameter.</p>"""
    default_values: NotRequired[
        "aws_sdk_quicksight.types.date_time_dataset_parameter_default_values.DateTimeDatasetParameterDefaultValues"
    ]
    """<p>A list of default values for a given date time parameter. This structure only accepts static values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateTimeDatasetParameter) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Name"] = value["name"]
    import aws_sdk_quicksight.types.dataset_parameter_value_type

    out["ValueType"] = (
        aws_sdk_quicksight.types.dataset_parameter_value_type.serialize_json(
            value["value_type"]
        )
    )
    if "time_granularity" in value:
        import aws_sdk_quicksight.types.time_granularity

        out["TimeGranularity"] = (
            aws_sdk_quicksight.types.time_granularity.serialize_json(
                value["time_granularity"]
            )
        )
    if "default_values" in value:
        import aws_sdk_quicksight.types.date_time_dataset_parameter_default_values

        out["DefaultValues"] = (
            aws_sdk_quicksight.types.date_time_dataset_parameter_default_values.serialize_json(
                value["default_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> DateTimeDatasetParameter:
    out: DateTimeDatasetParameter = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("DateTimeDatasetParameter.id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DateTimeDatasetParameter.name required")
    if "ValueType" in data:
        import aws_sdk_quicksight.types.dataset_parameter_value_type

        out["value_type"] = (
            aws_sdk_quicksight.types.dataset_parameter_value_type.deserialize_json(
                data["ValueType"]
            )
        )
    else:
        raise DeserializationError("DateTimeDatasetParameter.value_type required")
    if "TimeGranularity" in data:
        import aws_sdk_quicksight.types.time_granularity

        out["time_granularity"] = (
            aws_sdk_quicksight.types.time_granularity.deserialize_json(
                data["TimeGranularity"]
            )
        )
    if "DefaultValues" in data:
        import aws_sdk_quicksight.types.date_time_dataset_parameter_default_values

        out["default_values"] = (
            aws_sdk_quicksight.types.date_time_dataset_parameter_default_values.deserialize_json(
                data["DefaultValues"]
            )
        )
    return out
