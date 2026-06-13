"""Generated from Smithy shape ``com.amazonaws.entityresolution#CreateSchemaMappingInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.description
    import aws_sdk_entityresolution.types.entity_name
    import aws_sdk_entityresolution.types.schema_input_attributes
    import aws_sdk_entityresolution.types.tag_map


class CreateSchemaMappingInput(TypedDict):
    schema_name: "aws_sdk_entityresolution.types.entity_name.EntityName"
    """<p>The name of the schema. There can't be multiple <code>SchemaMappings</code> with the same name.</p>"""
    description: NotRequired["aws_sdk_entityresolution.types.description.Description"]
    """<p>A description of the schema.</p>"""
    mapped_input_fields: (
        "aws_sdk_entityresolution.types.schema_input_attributes.SchemaInputAttributes"
    )
    """<p>A list of <code>MappedInputFields</code>. Each <code>MappedInputField</code> corresponds to a column the source data table, and contains column name plus additional information that Entity Resolution uses for matching.</p>"""
    tags: NotRequired["aws_sdk_entityresolution.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSchemaMappingInput) -> dict:
    out: dict = {}
    out["schemaName"] = value["schema_name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_entityresolution.types.schema_input_attributes

    out["mappedInputFields"] = (
        aws_sdk_entityresolution.types.schema_input_attributes.serialize_json(
            value["mapped_input_fields"]
        )
    )
    if "tags" in value:
        import aws_sdk_entityresolution.types.tag_map

        out["tags"] = aws_sdk_entityresolution.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateSchemaMappingInput:
    out: CreateSchemaMappingInput = {}  # type: ignore[typeddict-item]
    if "schemaName" in data:
        out["schema_name"] = data["schemaName"]
    else:
        raise DeserializationError("CreateSchemaMappingInput.schema_name required")
    if "description" in data:
        out["description"] = data["description"]
    if "mappedInputFields" in data:
        import aws_sdk_entityresolution.types.schema_input_attributes

        out["mapped_input_fields"] = (
            aws_sdk_entityresolution.types.schema_input_attributes.deserialize_json(
                data["mappedInputFields"]
            )
        )
    else:
        raise DeserializationError(
            "CreateSchemaMappingInput.mapped_input_fields required"
        )
    if "tags" in data:
        import aws_sdk_entityresolution.types.tag_map

        out["tags"] = aws_sdk_entityresolution.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
