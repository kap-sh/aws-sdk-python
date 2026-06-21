"""Generated from Smithy shape ``com.amazonaws.elementalinference#FeedStatus``."""

from typing import Literal, TypeAlias, cast

FeedStatus: TypeAlias = Literal[
    "CREATING",
    "AVAILABLE",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "DELETED",
    "ARCHIVED",
]


# --- restJson1 ser/de ---
def serialize_json(value: FeedStatus) -> str:
    return value


def deserialize_json(data: str) -> FeedStatus:
    return cast(FeedStatus, data)
