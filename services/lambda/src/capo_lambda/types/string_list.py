"""Generated from Smithy shape ``com.amazonaws.lambda#StringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.string

StringList: TypeAlias = list["capo_lambda.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: StringList) -> list:
    return list(value)


def deserialize_json(data: list) -> StringList:
    return list(data)
