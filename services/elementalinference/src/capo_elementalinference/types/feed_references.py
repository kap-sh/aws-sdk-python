"""Generated from Smithy shape ``com.amazonaws.elementalinference#FeedReferences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elementalinference.types.feed_id

FeedReferences: TypeAlias = list["capo_elementalinference.types.feed_id.FeedId"]


# --- restJson1 ser/de ---
def serialize_json(value: FeedReferences) -> list:
    return list(value)


def deserialize_json(data: list) -> FeedReferences:
    return list(data)
