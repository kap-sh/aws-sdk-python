"""Generated from Smithy shape ``com.amazonaws.entityresolution#CreateSchemaMappingOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.description
    import aws_sdk_entityresolution.types.entity_name
    import aws_sdk_entityresolution.types.schema_input_attributes
    import aws_sdk_entityresolution.types.schema_mapping_arn


class CreateSchemaMappingOutput(TypedDict, closed=True):
    schema_name: "aws_sdk_entityresolution.types.entity_name.EntityName"
    """<p>The name of the schema.</p>"""
    schema_arn: "aws_sdk_entityresolution.types.schema_mapping_arn.SchemaMappingArn"
    """<p>The ARN (Amazon Resource Name) that Entity Resolution generated for the <code>SchemaMapping</code>.</p>"""
    description: "aws_sdk_entityresolution.types.description.Description"
    """<p>A description of the schema.</p>"""
    mapped_input_fields: (
        "aws_sdk_entityresolution.types.schema_input_attributes.SchemaInputAttributes"
    )
    """<p>A list of <code>MappedInputFields</code>. Each <code>MappedInputField</code> corresponds to a column the source data table, and contains column name plus additional information that Entity Resolution uses for matching.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSchemaMappingOutput) -> dict:
    out: dict = {}
    out["schemaName"] = value["schema_name"]
    out["schemaArn"] = value["schema_arn"]
    out["description"] = value["description"]
    import aws_sdk_entityresolution.types.schema_input_attributes

    out["mappedInputFields"] = (
        aws_sdk_entityresolution.types.schema_input_attributes.serialize_json(
            value["mapped_input_fields"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateSchemaMappingOutput:
    out: CreateSchemaMappingOutput = {}  # type: ignore[typeddict-item]
    if "schemaName" in data:
        out["schema_name"] = data["schemaName"]
    else:
        raise DeserializationError("CreateSchemaMappingOutput.schema_name required")
    if "schemaArn" in data:
        out["schema_arn"] = data["schemaArn"]
    else:
        raise DeserializationError("CreateSchemaMappingOutput.schema_arn required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("CreateSchemaMappingOutput.description required")
    if "mappedInputFields" in data:
        import aws_sdk_entityresolution.types.schema_input_attributes

        out["mapped_input_fields"] = (
            aws_sdk_entityresolution.types.schema_input_attributes.deserialize_json(
                data["mappedInputFields"]
            )
        )
    else:
        raise DeserializationError(
            "CreateSchemaMappingOutput.mapped_input_fields required"
        )
    return out
