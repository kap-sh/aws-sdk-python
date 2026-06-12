"""Generated from Smithy shape ``com.amazonaws.kafka#__listOf__stringMax249``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string_max249

__listOf__stringMax249: TypeAlias = list[
    "aws_sdk_kafka.types.__string_max249.__stringMax249"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOf__stringMax249) -> list:
    return list(value)


def deserialize_json(data: list) -> __listOf__stringMax249:
    return list(data)
