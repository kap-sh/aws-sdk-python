"""Generated from Smithy shape ``com.amazonaws.lambda#KafkaSchemaRegistryAccessConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lambda.types.kafka_schema_registry_access_config

KafkaSchemaRegistryAccessConfigList: TypeAlias = list[
    "aws_sdk_lambda.types.kafka_schema_registry_access_config.KafkaSchemaRegistryAccessConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: KafkaSchemaRegistryAccessConfigList) -> list:
    import aws_sdk_lambda.types.kafka_schema_registry_access_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lambda.types.kafka_schema_registry_access_config.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> KafkaSchemaRegistryAccessConfigList:
    import aws_sdk_lambda.types.kafka_schema_registry_access_config

    out: KafkaSchemaRegistryAccessConfigList = []
    for item in data:
        out.append(
            aws_sdk_lambda.types.kafka_schema_registry_access_config.deserialize_json(
                item
            )
        )
    return out
