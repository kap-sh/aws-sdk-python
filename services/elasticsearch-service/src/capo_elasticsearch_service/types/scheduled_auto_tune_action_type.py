"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ScheduledAutoTuneActionType``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies Auto-Tune action type. Valid values are JVM_HEAP_SIZE_TUNING and JVM_YOUNG_GEN_TUNING. </p>"""
ScheduledAutoTuneActionType: TypeAlias = Literal[
    "JVM_HEAP_SIZE_TUNING",
    "JVM_YOUNG_GEN_TUNING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScheduledAutoTuneActionType) -> str:
    return value


def deserialize_json(data: str) -> ScheduledAutoTuneActionType:
    return cast(ScheduledAutoTuneActionType, data)
