"""Generated from Smithy shape ``com.amazonaws.quicksight#ArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.arn

ArnList: TypeAlias = list["capo_quicksight.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: ArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> ArnList:
    return list(data)
