"""Generated from Smithy shape ``com.amazonaws.lambda#KafkaSchemaValidationAttribute``."""

from typing import Literal, TypeAlias, cast

KafkaSchemaValidationAttribute: TypeAlias = Literal[
    "KEY",
    "VALUE",
]


# --- restJson1 ser/de ---
def serialize_json(value: KafkaSchemaValidationAttribute) -> str:
    return value


def deserialize_json(data: str) -> KafkaSchemaValidationAttribute:
    return cast(KafkaSchemaValidationAttribute, data)
