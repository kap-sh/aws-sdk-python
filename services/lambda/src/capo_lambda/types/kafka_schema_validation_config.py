"""Generated from Smithy shape ``com.amazonaws.lambda#KafkaSchemaValidationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.kafka_schema_validation_attribute


class KafkaSchemaValidationConfig(TypedDict, closed=True):
    attribute: NotRequired[
        "capo_lambda.types.kafka_schema_validation_attribute.KafkaSchemaValidationAttribute"
    ]
    """<p> The attributes you want your schema registry to validate and filter for. If you selected <code>JSON</code> as the <code>EventRecordFormat</code>, Lambda also deserializes the selected message attributes. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaSchemaValidationConfig) -> dict:
    out: dict = {}
    if "attribute" in value:
        import capo_lambda.types.kafka_schema_validation_attribute

        out["Attribute"] = (
            capo_lambda.types.kafka_schema_validation_attribute.serialize_json(
                value["attribute"]
            )
        )
    return out


def deserialize_json(data: dict) -> KafkaSchemaValidationConfig:
    out: KafkaSchemaValidationConfig = {}  # type: ignore[typeddict-item]
    if data.get("Attribute") is not None:
        import capo_lambda.types.kafka_schema_validation_attribute

        out["attribute"] = (
            capo_lambda.types.kafka_schema_validation_attribute.deserialize_json(
                data["Attribute"]
            )
        )
    return out
