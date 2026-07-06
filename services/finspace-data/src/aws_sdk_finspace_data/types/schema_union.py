"""Generated from Smithy shape ``com.amazonaws.finspacedata#SchemaUnion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.schema_definition


class SchemaUnion(TypedDict, closed=True):
    tabular_schema_config: NotRequired[
        "aws_sdk_finspace_data.types.schema_definition.SchemaDefinition"
    ]
    """<p>The configuration for a schema on a tabular Dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchemaUnion) -> dict:
    out: dict = {}
    if "tabular_schema_config" in value:
        import aws_sdk_finspace_data.types.schema_definition

        out["tabularSchemaConfig"] = (
            aws_sdk_finspace_data.types.schema_definition.serialize_json(
                value["tabular_schema_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> SchemaUnion:
    out: SchemaUnion = {}  # type: ignore[typeddict-item]
    if "tabularSchemaConfig" in data:
        import aws_sdk_finspace_data.types.schema_definition

        out["tabular_schema_config"] = (
            aws_sdk_finspace_data.types.schema_definition.deserialize_json(
                data["tabularSchemaConfig"]
            )
        )
    return out
