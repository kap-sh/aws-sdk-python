"""Generated from Smithy shape ``com.amazonaws.quicksight#ErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.error_message

ErrorList: TypeAlias = list["aws_sdk_quicksight.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ErrorList) -> list:
    return list(value)


def deserialize_json(data: list) -> ErrorList:
    return list(data)
