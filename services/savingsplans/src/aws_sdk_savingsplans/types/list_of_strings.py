"""Generated from Smithy shape ``com.amazonaws.savingsplans#ListOfStrings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.string

ListOfStrings: TypeAlias = list["aws_sdk_savingsplans.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfStrings) -> list:
    return list(value)


def deserialize_json(data: list) -> ListOfStrings:
    return list(data)
