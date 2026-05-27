"""Generated from Smithy shape ``com.amazonaws.lambda#AmazonManagedKafkaEventSourceConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.kafka_schema_registry_config
    import aws_sdk_lambda.types.uri


class AmazonManagedKafkaEventSourceConfig(TypedDict):
    consumer_group_id: NotRequired["aws_sdk_lambda.types.uri.URI"]
    """<p>The identifier for the Kafka consumer group to join. The consumer group ID must be unique among all your Kafka event sources. After creating a Kafka event source mapping with the consumer group ID specified, you cannot update this value. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#services-msk-consumer-group-id\">Customizable consumer group ID</a>.</p>"""
    schema_registry_config: NotRequired[
        "aws_sdk_lambda.types.kafka_schema_registry_config.KafkaSchemaRegistryConfig"
    ]
    """<p>Specific configuration settings for a Kafka schema registry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmazonManagedKafkaEventSourceConfig) -> dict:
    out: dict = {}
    if "consumer_group_id" in value:
        out["ConsumerGroupId"] = value["consumer_group_id"]
    if "schema_registry_config" in value:
        import aws_sdk_lambda.types.kafka_schema_registry_config

        out["SchemaRegistryConfig"] = (
            aws_sdk_lambda.types.kafka_schema_registry_config.serialize_json(
                value["schema_registry_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> AmazonManagedKafkaEventSourceConfig:
    out: AmazonManagedKafkaEventSourceConfig = {}  # type: ignore[typeddict-item]
    if "ConsumerGroupId" in data:
        out["consumer_group_id"] = data["ConsumerGroupId"]
    if "SchemaRegistryConfig" in data:
        import aws_sdk_lambda.types.kafka_schema_registry_config

        out["schema_registry_config"] = (
            aws_sdk_lambda.types.kafka_schema_registry_config.deserialize_json(
                data["SchemaRegistryConfig"]
            )
        )
    return out
