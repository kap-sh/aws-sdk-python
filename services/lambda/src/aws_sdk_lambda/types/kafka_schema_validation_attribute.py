"""Generated from Smithy shape ``com.amazonaws.lambda#KafkaSchemaValidationAttribute``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_lambda.errors import DeserializationError

KafkaSchemaValidationAttribute: TypeAlias = Literal[
    "KEY",
    "VALUE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "KEY",
        "VALUE",
    )
)


def serialize_json(value: KafkaSchemaValidationAttribute) -> str:
    return value


def deserialize_json(data: str) -> KafkaSchemaValidationAttribute:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown KafkaSchemaValidationAttribute value: {data!r}"
        )
    return cast(KafkaSchemaValidationAttribute, data)
