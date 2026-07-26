"""Generated from Smithy shape ``com.amazonaws.quicksight#StringDatasetParameterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.string_dataset_parameter_default_value

StringDatasetParameterValueList: TypeAlias = list[
    "capo_quicksight.types.string_dataset_parameter_default_value.StringDatasetParameterDefaultValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: StringDatasetParameterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> StringDatasetParameterValueList:
    return list(data)
