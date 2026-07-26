"""Generated from Smithy shape ``com.amazonaws.appsync#FunctionsIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appsync.types.string

FunctionsIds: TypeAlias = list["capo_appsync.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionsIds) -> list:
    return list(value)


def deserialize_json(data: list) -> FunctionsIds:
    return list(data)
