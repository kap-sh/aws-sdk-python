"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetArnsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn

DataSetArnsList: TypeAlias = list["aws_sdk_quicksight.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: DataSetArnsList) -> list:
    return list(value)


def deserialize_json(data: list) -> DataSetArnsList:
    return list(data)
