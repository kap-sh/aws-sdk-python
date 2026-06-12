"""Generated from Smithy shape ``com.amazonaws.opensearch#ScheduledAutoTuneActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

"""<p>The Auto-Tune action type.</p>"""
ScheduledAutoTuneActionType: TypeAlias = Literal[
    "JVM_HEAP_SIZE_TUNING",
    "JVM_YOUNG_GEN_TUNING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "JVM_HEAP_SIZE_TUNING",
        "JVM_YOUNG_GEN_TUNING",
    )
)


def serialize_json(value: ScheduledAutoTuneActionType) -> str:
    return value


def deserialize_json(data: str) -> ScheduledAutoTuneActionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ScheduledAutoTuneActionType value: {data!r}"
        )
    return cast(ScheduledAutoTuneActionType, data)
