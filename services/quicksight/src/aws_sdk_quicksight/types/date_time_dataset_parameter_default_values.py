"""Generated from Smithy shape ``com.amazonaws.quicksight#DateTimeDatasetParameterDefaultValues``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.date_time_dataset_parameter_value_list


class DateTimeDatasetParameterDefaultValues(TypedDict):
    static_values: NotRequired[
        "aws_sdk_quicksight.types.date_time_dataset_parameter_value_list.DateTimeDatasetParameterValueList"
    ]
    """<p>A list of static default values for a given date time parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateTimeDatasetParameterDefaultValues) -> dict:
    out: dict = {}
    if "static_values" in value:
        import aws_sdk_quicksight.types.date_time_dataset_parameter_value_list

        out["StaticValues"] = (
            aws_sdk_quicksight.types.date_time_dataset_parameter_value_list.serialize_json(
                value["static_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> DateTimeDatasetParameterDefaultValues:
    out: DateTimeDatasetParameterDefaultValues = {}  # type: ignore[typeddict-item]
    if "StaticValues" in data:
        import aws_sdk_quicksight.types.date_time_dataset_parameter_value_list

        out["static_values"] = (
            aws_sdk_quicksight.types.date_time_dataset_parameter_value_list.deserialize_json(
                data["StaticValues"]
            )
        )
    return out
