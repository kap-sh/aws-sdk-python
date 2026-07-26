"""Generated from Smithy shape ``com.amazonaws.mediatailor#ListPrefetchScheduleType``."""

from typing import Literal, TypeAlias, cast

ListPrefetchScheduleType: TypeAlias = Literal[
    "SINGLE",
    "RECURRING",
    "ALL",
]


# --- restJson1 ser/de ---
def serialize_json(value: ListPrefetchScheduleType) -> str:
    return value


def deserialize_json(data: str) -> ListPrefetchScheduleType:
    return cast(ListPrefetchScheduleType, data)
