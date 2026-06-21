"""Generated from Smithy shape ``com.amazonaws.connect#SearchContactsTimeRangeConditionType``."""

from typing import Literal, TypeAlias, cast

SearchContactsTimeRangeConditionType: TypeAlias = Literal["NOT_EXISTS",]


# --- restJson1 ser/de ---
def serialize_json(value: SearchContactsTimeRangeConditionType) -> str:
    return value


def deserialize_json(data: str) -> SearchContactsTimeRangeConditionType:
    return cast(SearchContactsTimeRangeConditionType, data)
