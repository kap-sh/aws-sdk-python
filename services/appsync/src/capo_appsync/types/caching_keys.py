"""Generated from Smithy shape ``com.amazonaws.appsync#CachingKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appsync.types.string

CachingKeys: TypeAlias = list["capo_appsync.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: CachingKeys) -> list:
    return list(value)


def deserialize_json(data: list) -> CachingKeys:
    return list(data)
