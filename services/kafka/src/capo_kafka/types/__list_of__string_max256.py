"""Generated from Smithy shape ``com.amazonaws.kafka#__listOf__stringMax256``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kafka.types.__string_max256

__listOf__stringMax256: TypeAlias = list[
    "capo_kafka.types.__string_max256.__stringMax256"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOf__stringMax256) -> list:
    return list(value)


def deserialize_json(data: list) -> __listOf__stringMax256:
    return list(data)
