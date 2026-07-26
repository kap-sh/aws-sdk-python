"""Generated from Smithy shape ``com.amazonaws.opensearch#ScheduledAutoTuneActionType``."""

from typing import Literal, TypeAlias, cast

"""<p>The Auto-Tune action type.</p>"""
ScheduledAutoTuneActionType: TypeAlias = Literal[
    "JVM_HEAP_SIZE_TUNING",
    "JVM_YOUNG_GEN_TUNING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScheduledAutoTuneActionType) -> str:
    return value


def deserialize_json(data: str) -> ScheduledAutoTuneActionType:
    return cast(ScheduledAutoTuneActionType, data)
