"""Generated from Smithy shape ``com.amazonaws.quicksight#FoldersForResourceArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn

FoldersForResourceArnList: TypeAlias = list["aws_sdk_quicksight.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: FoldersForResourceArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> FoldersForResourceArnList:
    return list(data)
