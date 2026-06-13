"""Generated from Smithy shape ``com.amazonaws.quicksight#DataLabelTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_label_type

DataLabelTypes: TypeAlias = list[
    "aws_sdk_quicksight.types.data_label_type.DataLabelType"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataLabelTypes) -> list:
    import aws_sdk_quicksight.types.data_label_type

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.data_label_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataLabelTypes:
    import aws_sdk_quicksight.types.data_label_type

    out: DataLabelTypes = []
    for item in data:
        out.append(aws_sdk_quicksight.types.data_label_type.deserialize_json(item))
    return out
