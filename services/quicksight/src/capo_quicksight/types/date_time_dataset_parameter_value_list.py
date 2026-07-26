"""Generated from Smithy shape ``com.amazonaws.quicksight#DateTimeDatasetParameterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.date_time_dataset_parameter_default_value

DateTimeDatasetParameterValueList: TypeAlias = list[
    "capo_quicksight.types.date_time_dataset_parameter_default_value.DateTimeDatasetParameterDefaultValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: DateTimeDatasetParameterValueList) -> list:
    import capo_quicksight.types.date_time_dataset_parameter_default_value

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.date_time_dataset_parameter_default_value.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DateTimeDatasetParameterValueList:
    import capo_quicksight.types.date_time_dataset_parameter_default_value

    out: DateTimeDatasetParameterValueList = []
    for item in data:
        out.append(
            capo_quicksight.types.date_time_dataset_parameter_default_value.deserialize_json(
                item
            )
        )
    return out
