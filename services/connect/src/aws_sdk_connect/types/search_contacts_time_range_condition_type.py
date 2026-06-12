"""Generated from Smithy shape ``com.amazonaws.connect#SearchContactsTimeRangeConditionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

SearchContactsTimeRangeConditionType: TypeAlias = Literal["NOT_EXISTS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("NOT_EXISTS",))


def serialize_json(value: SearchContactsTimeRangeConditionType) -> str:
    return value


def deserialize_json(data: str) -> SearchContactsTimeRangeConditionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SearchContactsTimeRangeConditionType value: {data!r}"
        )
    return cast(SearchContactsTimeRangeConditionType, data)
