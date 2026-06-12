"""Generated from Smithy shape ``com.amazonaws.glue#EntityConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.field_definition_map
    import aws_sdk_glue.types.source_configuration


class EntityConfiguration(TypedDict):
    source_configuration: NotRequired[
        "aws_sdk_glue.types.source_configuration.SourceConfiguration"
    ]
    """<p>The source configuration that defines how to make requests to access this entity's data through the REST API.</p>"""
    schema: NotRequired["aws_sdk_glue.types.field_definition_map.FieldDefinitionMap"]
    """<p>The schema definition for this entity, including field names, types, and other metadata that describes the structure of the data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityConfiguration) -> dict:
    out: dict = {}
    if "source_configuration" in value:
        import aws_sdk_glue.types.source_configuration

        out["SourceConfiguration"] = (
            aws_sdk_glue.types.source_configuration.serialize_aws_json_1_1(
                value["source_configuration"]
            )
        )
    if "schema" in value:
        import aws_sdk_glue.types.field_definition_map

        out["Schema"] = aws_sdk_glue.types.field_definition_map.serialize_aws_json_1_1(
            value["schema"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityConfiguration:
    out: EntityConfiguration = {}  # type: ignore[typeddict-item]
    if "SourceConfiguration" in data:
        import aws_sdk_glue.types.source_configuration

        out["source_configuration"] = (
            aws_sdk_glue.types.source_configuration.deserialize_aws_json_1_1(
                data["SourceConfiguration"]
            )
        )
    if "Schema" in data:
        import aws_sdk_glue.types.field_definition_map

        out["schema"] = (
            aws_sdk_glue.types.field_definition_map.deserialize_aws_json_1_1(
                data["Schema"]
            )
        )
    return out
