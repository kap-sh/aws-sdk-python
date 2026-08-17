"""Generated from Smithy shape ``com.amazonaws.lambda#KafkaSchemaRegistryConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.kafka_schema_registry_access_config_list
    import capo_lambda.types.kafka_schema_validation_config_list
    import capo_lambda.types.schema_registry_event_record_format
    import capo_lambda.types.schema_registry_uri


class KafkaSchemaRegistryConfig(TypedDict, closed=True):
    schema_registry_uri: NotRequired[
        "capo_lambda.types.schema_registry_uri.SchemaRegistryUri"
    ]
    """<p>The URI for your schema registry. The correct URI format depends on the type of schema registry you're using.</p> <ul> <li> <p>For Glue schema registries, use the ARN of the registry.</p> </li> <li> <p>For Confluent schema registries, use the URL of the registry.</p> </li> </ul>"""
    event_record_format: NotRequired[
        "capo_lambda.types.schema_registry_event_record_format.SchemaRegistryEventRecordFormat"
    ]
    """<p>The record format that Lambda delivers to your function after schema validation.</p> <ul> <li> <p>Choose <code>JSON</code> to have Lambda deliver the record to your function as a standard JSON object.</p> </li> <li> <p>Choose <code>SOURCE</code> to have Lambda deliver the record to your function in its original source format. Lambda removes all schema metadata, such as the schema ID, before sending the record to your function.</p> </li> </ul>"""
    access_configs: NotRequired[
        "capo_lambda.types.kafka_schema_registry_access_config_list.KafkaSchemaRegistryAccessConfigList"
    ]
    """<p>An array of access configuration objects that tell Lambda how to authenticate with your schema registry.</p>"""
    schema_validation_configs: NotRequired[
        "capo_lambda.types.kafka_schema_validation_config_list.KafkaSchemaValidationConfigList"
    ]
    """<p>An array of schema validation configuration objects, which tell Lambda the message attributes you want to validate and filter using your schema registry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaSchemaRegistryConfig) -> dict:
    out: dict = {}
    if "schema_registry_uri" in value:
        out["SchemaRegistryURI"] = value["schema_registry_uri"]
    if "event_record_format" in value:
        import capo_lambda.types.schema_registry_event_record_format

        out["EventRecordFormat"] = (
            capo_lambda.types.schema_registry_event_record_format.serialize_json(
                value["event_record_format"]
            )
        )
    if "access_configs" in value:
        import capo_lambda.types.kafka_schema_registry_access_config_list

        out["AccessConfigs"] = (
            capo_lambda.types.kafka_schema_registry_access_config_list.serialize_json(
                value["access_configs"]
            )
        )
    if "schema_validation_configs" in value:
        import capo_lambda.types.kafka_schema_validation_config_list

        out["SchemaValidationConfigs"] = (
            capo_lambda.types.kafka_schema_validation_config_list.serialize_json(
                value["schema_validation_configs"]
            )
        )
    return out


def deserialize_json(data: dict) -> KafkaSchemaRegistryConfig:
    out: KafkaSchemaRegistryConfig = {}  # type: ignore[typeddict-item]
    if data.get("SchemaRegistryURI") is not None:
        out["schema_registry_uri"] = data["SchemaRegistryURI"]
    if data.get("EventRecordFormat") is not None:
        import capo_lambda.types.schema_registry_event_record_format

        out["event_record_format"] = (
            capo_lambda.types.schema_registry_event_record_format.deserialize_json(
                data["EventRecordFormat"]
            )
        )
    if data.get("AccessConfigs") is not None:
        import capo_lambda.types.kafka_schema_registry_access_config_list

        out["access_configs"] = (
            capo_lambda.types.kafka_schema_registry_access_config_list.deserialize_json(
                data["AccessConfigs"]
            )
        )
    if data.get("SchemaValidationConfigs") is not None:
        import capo_lambda.types.kafka_schema_validation_config_list

        out["schema_validation_configs"] = (
            capo_lambda.types.kafka_schema_validation_config_list.deserialize_json(
                data["SchemaValidationConfigs"]
            )
        )
    return out
