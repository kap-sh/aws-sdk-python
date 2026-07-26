"""Generated from Smithy shape ``com.amazonaws.glue#CheckSchemaVersionValidityInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.data_format
    import capo_glue.types.schema_definition_string


class CheckSchemaVersionValidityInput(TypedDict, closed=True):
    data_format: "capo_glue.types.data_format.DataFormat"
    """<p>The data format of the schema definition. Currently <code>AVRO</code>, <code>JSON</code> and <code>PROTOBUF</code> are supported.</p>"""
    schema_definition: "capo_glue.types.schema_definition_string.SchemaDefinitionString"
    """<p>The definition of the schema that has to be validated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CheckSchemaVersionValidityInput) -> dict:
    out: dict = {}
    import capo_glue.types.data_format

    out["DataFormat"] = capo_glue.types.data_format.serialize_aws_json_1_1(
        value["data_format"]
    )
    out["SchemaDefinition"] = value["schema_definition"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CheckSchemaVersionValidityInput:
    out: CheckSchemaVersionValidityInput = {}  # type: ignore[typeddict-item]
    if "DataFormat" in data:
        import capo_glue.types.data_format

        out["data_format"] = capo_glue.types.data_format.deserialize_aws_json_1_1(
            data["DataFormat"]
        )
    else:
        raise DeserializationError(
            "CheckSchemaVersionValidityInput.data_format required"
        )
    if "SchemaDefinition" in data:
        out["schema_definition"] = data["SchemaDefinition"]
    else:
        raise DeserializationError(
            "CheckSchemaVersionValidityInput.schema_definition required"
        )
    return out
