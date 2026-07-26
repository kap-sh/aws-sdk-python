"""Generated from Smithy shape ``com.amazonaws.quicksight#Path``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.arn

Path: TypeAlias = list["capo_quicksight.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: Path) -> list:
    return list(value)


def deserialize_json(data: list) -> Path:
    return list(data)
