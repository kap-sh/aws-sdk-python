"""Generated from Smithy shape ``com.amazonaws.mediatailor#PrefetchScheduleType``."""

from typing import Literal, TypeAlias, cast

PrefetchScheduleType: TypeAlias = Literal[
    "SINGLE",
    "RECURRING",
]


# --- restJson1 ser/de ---
def serialize_json(value: PrefetchScheduleType) -> str:
    return value


def deserialize_json(data: str) -> PrefetchScheduleType:
    return cast(PrefetchScheduleType, data)
