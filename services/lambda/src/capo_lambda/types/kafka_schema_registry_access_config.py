"""Generated from Smithy shape ``com.amazonaws.lambda#KafkaSchemaRegistryAccessConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.arn
    import capo_lambda.types.kafka_schema_registry_auth_type


class KafkaSchemaRegistryAccessConfig(TypedDict, closed=True):
    type: NotRequired[
        "capo_lambda.types.kafka_schema_registry_auth_type.KafkaSchemaRegistryAuthType"
    ]
    """<p> The type of authentication Lambda uses to access your schema registry. </p>"""
    uri: NotRequired["capo_lambda.types.arn.Arn"]
    """<p> The URI of the secret (Secrets Manager secret ARN) to authenticate with your schema registry. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaSchemaRegistryAccessConfig) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_lambda.types.kafka_schema_registry_auth_type

        out["Type"] = capo_lambda.types.kafka_schema_registry_auth_type.serialize_json(
            value["type"]
        )
    if "uri" in value:
        out["URI"] = value["uri"]
    return out


def deserialize_json(data: dict) -> KafkaSchemaRegistryAccessConfig:
    out: KafkaSchemaRegistryAccessConfig = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_lambda.types.kafka_schema_registry_auth_type

        out["type"] = (
            capo_lambda.types.kafka_schema_registry_auth_type.deserialize_json(
                data["Type"]
            )
        )
    if "URI" in data:
        out["uri"] = data["URI"]
    return out
