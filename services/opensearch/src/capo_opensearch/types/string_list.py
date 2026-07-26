"""Generated from Smithy shape ``com.amazonaws.opensearch#StringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.string

StringList: TypeAlias = list["capo_opensearch.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: StringList) -> list:
    return list(value)


def deserialize_json(data: list) -> StringList:
    return list(data)
