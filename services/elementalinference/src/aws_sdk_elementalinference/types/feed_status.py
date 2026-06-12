"""Generated from Smithy shape ``com.amazonaws.elementalinference#FeedStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elementalinference.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "AVAILABLE",
        "ACTIVE",
        "UPDATING",
        "DELETING",
        "DELETED",
        "ARCHIVED",
    )
)


def serialize_json(value: FeedStatus) -> str:
    return value


def deserialize_json(data: str) -> FeedStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FeedStatus value: {data!r}")
    return cast(FeedStatus, data)
