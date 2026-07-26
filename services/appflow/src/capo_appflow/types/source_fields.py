"""Generated from Smithy shape ``com.amazonaws.appflow#SourceFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appflow.types.string

SourceFields: TypeAlias = list["capo_appflow.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: SourceFields) -> list:
    return list(value)


def deserialize_json(data: list) -> SourceFields:
    return list(data)
