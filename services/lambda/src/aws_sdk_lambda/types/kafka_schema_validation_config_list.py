"""Generated from Smithy shape ``com.amazonaws.lambda#KafkaSchemaValidationConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lambda.types.kafka_schema_validation_config

KafkaSchemaValidationConfigList: TypeAlias = list[
    "aws_sdk_lambda.types.kafka_schema_validation_config.KafkaSchemaValidationConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: KafkaSchemaValidationConfigList) -> list:
    import aws_sdk_lambda.types.kafka_schema_validation_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lambda.types.kafka_schema_validation_config.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> KafkaSchemaValidationConfigList:
    import aws_sdk_lambda.types.kafka_schema_validation_config

    out: KafkaSchemaValidationConfigList = []
    for item in data:
        out.append(
            aws_sdk_lambda.types.kafka_schema_validation_config.deserialize_json(item)
        )
    return out
