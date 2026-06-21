"""Generated from Smithy shape ``com.amazonaws.connect#SearchableQueueType``."""

from typing import Literal, TypeAlias, cast

SearchableQueueType: TypeAlias = Literal["STANDARD",]


# --- restJson1 ser/de ---
def serialize_json(value: SearchableQueueType) -> str:
    return value


def deserialize_json(data: str) -> SearchableQueueType:
    return cast(SearchableQueueType, data)
