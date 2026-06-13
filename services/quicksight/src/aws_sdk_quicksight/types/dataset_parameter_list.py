"""Generated from Smithy shape ``com.amazonaws.quicksight#DatasetParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dataset_parameter

DatasetParameterList: TypeAlias = list[
    "aws_sdk_quicksight.types.dataset_parameter.DatasetParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetParameterList) -> list:
    import aws_sdk_quicksight.types.dataset_parameter

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.dataset_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> DatasetParameterList:
    import aws_sdk_quicksight.types.dataset_parameter

    out: DatasetParameterList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.dataset_parameter.deserialize_json(item))
    return out
