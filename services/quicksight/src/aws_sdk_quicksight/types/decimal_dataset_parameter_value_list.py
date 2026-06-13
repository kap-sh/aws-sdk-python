"""Generated from Smithy shape ``com.amazonaws.quicksight#DecimalDatasetParameterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.decimal_dataset_parameter_default_value

DecimalDatasetParameterValueList: TypeAlias = list[
    "aws_sdk_quicksight.types.decimal_dataset_parameter_default_value.DecimalDatasetParameterDefaultValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: DecimalDatasetParameterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> DecimalDatasetParameterValueList:
    return list(data)
