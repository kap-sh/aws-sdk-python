"""Generated from Smithy shape ``com.amazonaws.quicksight#AuthorizedTargetsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.string

AuthorizedTargetsList: TypeAlias = list["aws_sdk_quicksight.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizedTargetsList) -> list:
    return list(value)


def deserialize_json(data: list) -> AuthorizedTargetsList:
    return list(data)
