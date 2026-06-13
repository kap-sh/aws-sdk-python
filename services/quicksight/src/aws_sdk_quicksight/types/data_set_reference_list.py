"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_reference

DataSetReferenceList: TypeAlias = list[
    "aws_sdk_quicksight.types.data_set_reference.DataSetReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSetReferenceList) -> list:
    import aws_sdk_quicksight.types.data_set_reference

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.data_set_reference.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSetReferenceList:
    import aws_sdk_quicksight.types.data_set_reference

    out: DataSetReferenceList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.data_set_reference.deserialize_json(item))
    return out
