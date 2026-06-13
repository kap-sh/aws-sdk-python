"""Generated from Smithy shape ``com.amazonaws.quicksight#DateTimeDatasetParameterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.date_time_dataset_parameter_default_value

DateTimeDatasetParameterValueList: TypeAlias = list[
    "aws_sdk_quicksight.types.date_time_dataset_parameter_default_value.DateTimeDatasetParameterDefaultValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: DateTimeDatasetParameterValueList) -> list:
    import aws_sdk_quicksight.types.date_time_dataset_parameter_default_value

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.date_time_dataset_parameter_default_value.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DateTimeDatasetParameterValueList:
    import aws_sdk_quicksight.types.date_time_dataset_parameter_default_value

    out: DateTimeDatasetParameterValueList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.date_time_dataset_parameter_default_value.deserialize_json(
                item
            )
        )
    return out
