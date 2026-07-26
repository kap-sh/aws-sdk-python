"""Generated from Smithy shape ``com.amazonaws.lambda#KafkaSchemaValidationConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.kafka_schema_validation_config

KafkaSchemaValidationConfigList: TypeAlias = list[
    "capo_lambda.types.kafka_schema_validation_config.KafkaSchemaValidationConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: KafkaSchemaValidationConfigList) -> list:
    import capo_lambda.types.kafka_schema_validation_config

    out: list = []
    for item in value:
        out.append(
            capo_lambda.types.kafka_schema_validation_config.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> KafkaSchemaValidationConfigList:
    import capo_lambda.types.kafka_schema_validation_config

    out: KafkaSchemaValidationConfigList = []
    for item in data:
        out.append(
            capo_lambda.types.kafka_schema_validation_config.deserialize_json(item)
        )
    return out
