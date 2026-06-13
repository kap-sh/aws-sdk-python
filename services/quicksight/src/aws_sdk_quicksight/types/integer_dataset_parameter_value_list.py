"""Generated from Smithy shape ``com.amazonaws.quicksight#IntegerDatasetParameterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.integer_dataset_parameter_default_value

IntegerDatasetParameterValueList: TypeAlias = list[
    "aws_sdk_quicksight.types.integer_dataset_parameter_default_value.IntegerDatasetParameterDefaultValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntegerDatasetParameterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> IntegerDatasetParameterValueList:
    return list(data)
