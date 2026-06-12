"""Generated from Smithy shape ``com.amazonaws.connect#SearchableQueueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

SearchableQueueType: TypeAlias = Literal["STANDARD",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("STANDARD",))


def serialize_json(value: SearchableQueueType) -> str:
    return value


def deserialize_json(data: str) -> SearchableQueueType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SearchableQueueType value: {data!r}")
    return cast(SearchableQueueType, data)
